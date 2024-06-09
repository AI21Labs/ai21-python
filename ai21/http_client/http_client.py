from typing import Optional, Dict, Any, BinaryIO

import httpx
from httpx import ConnectError
from tenacity import retry, retry_if_result, stop_after_attempt, wait_exponential, RetryError

from ai21.logger import logger
from ai21.stream.stream import Stream
from ai21.http_client.base_http_client import (
    BaseHttpClient,
    handle_non_success_response,
    RETRY_BACK_OFF_FACTOR,
    TIME_BETWEEN_RETRIES,
)


def _requests_retry_session(retries: int) -> httpx.HTTPTransport:
    return httpx.HTTPTransport(
        retries=retries,
    )


class HttpClient(BaseHttpClient[httpx.Client, Stream[Any]]):
    def __init__(
        self,
        client: Optional[httpx.Client] = None,
        timeout_sec: int = None,
        num_retries: int = None,
        headers: Dict = None,
    ):
        super().__init__(timeout_sec=timeout_sec, num_retries=num_retries, headers=headers)
        self._client = self._init_client(client)

        # Since we can't use the retry decorator on a method of a class as we can't access class attributes,
        # we have to wrap the method in a function
        self._request = retry(
            wait=wait_exponential(multiplier=RETRY_BACK_OFF_FACTOR, min=TIME_BETWEEN_RETRIES),
            retry=retry_if_result(self._should_retry),
            stop=stop_after_attempt(self._num_retries),
        )(self._request)

    def execute_http_request(
        self,
        method: str,
        url: str,
        params: Optional[Dict] = None,
        body: Optional[Dict] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
    ) -> httpx.Response:
        try:
            response = self._request(files=files, method=method, params=params, url=url, stream=stream, body=body)
        except RetryError as retry_error:
            last_attempt = retry_error.last_attempt

            if last_attempt.failed:
                raise last_attempt.exception()
            else:
                response = last_attempt.result()

        except ConnectError as connection_error:
            logger.error(f"Calling {method} {url} failed with ConnectionError: {connection_error}")
            raise connection_error
        except Exception as exception:
            logger.error(f"Calling {method} {url} failed with Exception: {exception}")
            raise exception

        if response.status_code != httpx.codes.OK:
            logger.error(f"Calling {method} {url} failed with a non-200 response code: {response.status_code}")
            handle_non_success_response(response.status_code, response.text)

        return response

    def _request(
        self,
        files: Optional[Dict[str, BinaryIO]],
        method: str,
        params: Optional[Dict],
        body: Optional[Dict],
        url: str,
        stream: bool,
    ) -> httpx.Response:
        timeout = self._timeout_sec
        headers = self._headers
        logger.debug(f"Calling {method} {url} {headers} {params}")

        if method == "GET":
            request = self._client.build_request(
                method=method,
                url=url,
                headers=headers,
                timeout=timeout,
                params=params,
            )

            return self._client.send(request=request, stream=stream)

        data = self._get_request_data(files=files, method=method, body=body)
        headers = self._get_request_headers(files=files)

        request = self._client.build_request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            data=data,
            timeout=timeout,
            files=files,
        )

        return self._client.send(request=request, stream=stream)

    def _init_client(self, client: Optional[httpx.Client]) -> httpx.Client:
        if client is not None:
            return client

        if self._apply_retry_policy:
            return httpx.Client(transport=_requests_retry_session(retries=self._num_retries))

        return httpx.Client()
