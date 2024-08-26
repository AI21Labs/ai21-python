import logging
from typing import Any, Optional, Dict, BinaryIO
from tenacity import retry, retry_if_result, stop_after_attempt, wait_exponential, RetryError
from httpx import ConnectError

import httpx

from ai21.logger import logger
from ai21.models.request_options import RequestOptions
from ai21.stream.async_stream import AsyncStream
from ai21.http_client.base_http_client import (
    BaseHttpClient,
    handle_non_success_response,
    RETRY_BACK_OFF_FACTOR,
    TIME_BETWEEN_RETRIES,
)
from ai21.stream.stream_commons import _SSEDecoder

_logger = logging.getLogger(__name__)


def _requests_retry_async_session(retries: int) -> httpx.AsyncHTTPTransport:
    return httpx.AsyncHTTPTransport(
        retries=retries,
    )


class AsyncAI21HTTPClient(BaseHttpClient[httpx.AsyncClient, AsyncStream[Any]]):
    def __init__(
        self,
        api_key: Optional[str] = None,
        requires_api_key: bool = True,
        client: Optional[httpx.AsyncClient] = None,
        timeout_sec: int = None,
        num_retries: int = None,
        headers: Dict = None,
        via: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            requires_api_key=requires_api_key,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            headers=headers,
            via=via,
        )
        self._client = self._init_client(client)
        self._headers = self._build_headers(passed_headers=headers)

        # Since we can't use the retry decorator on a method of a class as we can't access class attributes,
        # we have to wrap the method in a function
        self._request = retry(
            wait=wait_exponential(multiplier=RETRY_BACK_OFF_FACTOR, min=TIME_BETWEEN_RETRIES),
            retry=retry_if_result(self._should_retry),
            stop=stop_after_attempt(self._num_retries),
        )(self._run_request)
        self._streaming_decoder = _SSEDecoder()

    async def execute_http_request(
        self,
        method: str,
        path: Optional[str] = None,
        params: Optional[Dict] = None,
        body: Optional[Dict] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
        extra_headers: Optional[Dict] = None,
    ) -> httpx.Response:
        headers = {**self._headers, **extra_headers} if extra_headers is not None else self._headers

        options = RequestOptions(
            path=path,
            body=body,
            method=method,
            stream=stream,
            params=params,
            files=files,
            headers=headers,
            timeout=self._timeout_sec,
            url=self._base_url,
        )

        try:
            response = await self._request(options=options)
        except RetryError as retry_error:
            last_attempt = retry_error.last_attempt

            if last_attempt.failed:
                raise last_attempt.exception()
            else:
                response = last_attempt.result()

        except ConnectError as connection_error:
            logger.error(f"Calling {method} {self._base_url} failed with ConnectionError: {connection_error}")
            raise connection_error
        except Exception as exception:
            logger.error(f"Calling {method} {self._base_url} failed with Exception: {exception}")
            raise exception

        if response.status_code != httpx.codes.OK:
            logger.error(
                f"Calling {method} {self._base_url} failed with a non-200 response code: {response.status_code}"
            )

            if stream:
                details = self._extract_streaming_error_details(response)
                handle_non_success_response(response.status_code, details)
            else:
                handle_non_success_response(response.status_code, response.text)

        return response

    async def _run_request(self, options: RequestOptions) -> httpx.Response:
        request = self._build_request(options)

        _logger.debug(f"Calling {request.method} {request.url} {request.headers}, {options.body}")
        return await self._client.send(request=request, stream=options.stream)

    def _init_client(self, client: Optional[httpx.AsyncClient]) -> httpx.AsyncClient:
        if client is not None:
            return client

        if self._apply_retry_policy:
            return httpx.AsyncClient(transport=_requests_retry_async_session(retries=self._num_retries))

        return httpx.AsyncClient()

    def _get_streaming_decoder(self) -> _SSEDecoder:
        return self._streaming_decoder
