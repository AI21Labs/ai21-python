import logging
from typing import Optional, Dict, Any, BinaryIO

import httpx
from httpx import ConnectError
from tenacity import retry, retry_if_result, stop_after_attempt, wait_exponential, RetryError

from ai21.http_client.base_http_client import (
    BaseHttpClient,
    handle_non_success_response,
    RETRY_BACK_OFF_FACTOR,
    TIME_BETWEEN_RETRIES,
)
from ai21.stream.stream import Stream

_logger = logging.getLogger(__name__)


def _requests_retry_session(retries: int) -> httpx.HTTPTransport:
    return httpx.HTTPTransport(
        retries=retries,
    )


class AI21HTTPClient(BaseHttpClient[httpx.Client, Stream[Any]]):
    def __init__(
        self,
        api_key: Optional[str] = None,
        client: Optional[httpx.Client] = None,
        timeout_sec: int = None,
        num_retries: int = None,
        headers: Dict = None,
        via: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        super().__init__(timeout_sec=timeout_sec, num_retries=num_retries, headers=headers, via=via)
        self._api_key = api_key
        self._base_url = base_url
        self._client = self._init_client(client)
        self._headers = self._build_headers(passed_headers=headers)

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
        path: str,
        params: Optional[Dict] = None,
        body: Optional[Dict] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
        extra_headers: Optional[Dict] = None,
    ) -> httpx.Response:
        try:
            options = {"path": path, "body": body, "params": params, "stream": stream, "files": files, "method": method}

            response = self._request(
                options=options,
                extra_headers=extra_headers,
            )
        except RetryError as retry_error:
            last_attempt = retry_error.last_attempt

            if last_attempt.failed:
                raise last_attempt.exception()
            else:
                response = last_attempt.result()

        except ConnectError as connection_error:
            _logger.error(f"Calling {method} {self._base_url} failed with ConnectionError: {connection_error}")
            raise connection_error
        except Exception as exception:
            _logger.error(f"Calling {method} {self._base_url} failed with Exception: {exception}")
            raise exception

        if response.status_code != httpx.codes.OK:
            _logger.error(
                f"Calling {method} {self._base_url} failed with a non-200 response code: {response.status_code}"
            )
            handle_non_success_response(response.status_code, response.text)

        return response

    def _request(
        self,
        options: Dict[str, Any],
        extra_headers: Optional[Dict],
    ) -> httpx.Response:
        timeout = self._timeout_sec
        headers = {**self._headers, **extra_headers} if extra_headers is not None else self._headers

        options["url"] = self._base_url
        options["headers"] = headers
        options["timeout"] = timeout
        request = self._build_request(options)

        _logger.debug(f"Calling {request.method} {request.url} {request.headers}, {options.get('body')}")
        return self._client.send(request=request, stream=options["stream"])

    def _init_client(self, client: Optional[httpx.Client]) -> httpx.Client:
        if client is not None:
            return client

        if self._apply_retry_policy:
            return httpx.Client(transport=_requests_retry_session(retries=self._num_retries))

        return httpx.Client()
