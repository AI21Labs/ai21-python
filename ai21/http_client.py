import json
from typing import Optional, Dict, Any, BinaryIO

import httpx
from httpx import ConnectError
from tenacity import retry, retry_if_result, stop_after_attempt, wait_exponential, RetryError

from ai21.errors import (
    BadRequest,
    Unauthorized,
    UnprocessableEntity,
    TooManyRequestsError,
    AI21ServerError,
    ServiceUnavailable,
    AI21APIError,
)
from ai21.logger import logger

DEFAULT_TIMEOUT_SEC = 300
DEFAULT_NUM_RETRIES = 0
RETRY_BACK_OFF_FACTOR = 0.5
TIME_BETWEEN_RETRIES = 1
RETRY_ERROR_CODES = (408, 429, 500, 503)
RETRY_METHOD_WHITELIST = ["GET", "POST", "PUT"]


def handle_non_success_response(status_code: int, response_text: str):
    if status_code == 400:
        raise BadRequest(details=response_text)
    if status_code == 401:
        raise Unauthorized(details=response_text)
    if status_code == 422:
        raise UnprocessableEntity(details=response_text)
    if status_code == 429:
        raise TooManyRequestsError(details=response_text)
    if status_code == 500:
        raise AI21ServerError(details=response_text)
    if status_code == 503:
        raise ServiceUnavailable(details=response_text)
    raise AI21APIError(status_code, details=response_text)


def _requests_retry_session(retries: int) -> httpx.HTTPTransport:
    return httpx.HTTPTransport(
        retries=retries,
    )


class HttpClient:
    def __init__(
        self,
        client: Optional[httpx.Client] = None,
        timeout_sec: int = None,
        num_retries: int = None,
        headers: Dict = None,
    ):
        self._timeout_sec = timeout_sec or DEFAULT_TIMEOUT_SEC
        self._num_retries = num_retries or DEFAULT_NUM_RETRIES
        self._headers = headers or {}
        self._apply_retry_policy = self._num_retries > 0
        self._client = self._init_client(client)

        # Since we can't use the retry decorator on a method of a class as we can't access class attributes,
        # we have to wrap the method in a function
        self._request = retry(
            wait=wait_exponential(multiplier=RETRY_BACK_OFF_FACTOR, min=TIME_BETWEEN_RETRIES),
            retry=retry_if_result(self._should_retry),
            stop=stop_after_attempt(self._num_retries),
        )(self._request)

    def _should_retry(self, response: httpx.Response) -> bool:
        return response.status_code in RETRY_ERROR_CODES and response.request.method in RETRY_METHOD_WHITELIST

    def execute_http_request(
        self,
        method: str,
        url: str,
        params: Optional[Dict] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
    ) -> httpx.Response:
        try:
            response = self._request(files=files, method=method, params=params, url=url, stream=stream)
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
        url: str,
        stream: bool,
    ) -> httpx.Response:
        timeout = self._timeout_sec
        headers = self._headers
        logger.debug(f"Calling {method} {url} {headers} {params}")

        if method == "GET":
            request = self._client.build_request(
                method=method, url=url, headers=headers, timeout=timeout, params=params
            )

            return self._client.send(request=request, stream=stream)

        if files is not None:
            if method != "POST":
                raise ValueError(
                    f"execute_http_request supports only POST for files upload, but {method} was supplied instead"
                )
            if "Content-Type" in headers:
                headers.pop(
                    "Content-Type"
                )  # multipart/form-data 'Content-Type' is being added when passing rb files and payload
            data = params
        else:
            data = json.dumps(params).encode() if params else None

        request = self._client.build_request(
            method=method,
            url=url,
            headers=headers,
            data=data,
            timeout=timeout,
            files=files,
        )

        return self._client.send(request=request, stream=stream)

    def _init_client(self, client: Optional[httpx.Client]) -> httpx.Client:
        if client is not None:
            return client

        return _requests_retry_session(retries=self._num_retries) if self._apply_retry_policy else httpx.Client()

    def add_headers(self, headers: Dict[str, Any]) -> None:
        self._headers.update(headers)
