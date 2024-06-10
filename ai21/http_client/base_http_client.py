from __future__ import annotations

import json

from typing import Generic, TypeVar, Union, Any, Optional, Dict, BinaryIO
from abc import ABC, abstractmethod

import httpx

from ai21.stream.stream import Stream
from ai21.stream.async_stream import AsyncStream
from ai21.errors import (
    BadRequest,
    Unauthorized,
    UnprocessableEntity,
    TooManyRequestsError,
    AI21ServerError,
    ServiceUnavailable,
    AI21APIError,
)

_HttpxClientT = TypeVar("_HttpxClientT", bound=Union[httpx.Client, httpx.AsyncClient])
_DefaultStreamT = TypeVar("_DefaultStreamT", bound=Union[Stream[Any], AsyncStream[Any]])


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


class BaseHttpClient(ABC, Generic[_HttpxClientT, _DefaultStreamT]):
    _client: Optional[_HttpxClientT] = None
    _request: Any

    def __init__(
        self,
        timeout_sec: int = None,
        num_retries: int = None,
        headers: Dict = None,
    ):
        self._timeout_sec = timeout_sec or DEFAULT_TIMEOUT_SEC
        self._num_retries = num_retries or DEFAULT_NUM_RETRIES
        self._headers = headers or {}
        self._apply_retry_policy = self._num_retries > 0

    def _should_retry(self, response: httpx.Response) -> bool:
        return response.status_code in RETRY_ERROR_CODES and response.request.method in RETRY_METHOD_WHITELIST

    def _get_request_data(
        self,
        files: Optional[Dict[str, BinaryIO]],
        method: str,
        body=Optional[Dict],
    ) -> Dict[str, Any] | bytes:
        if files is not None:
            if method != "POST":
                raise ValueError(
                    f"execute_http_request supports only POST for files upload, but {method} was supplied instead"
                )

            return body
        else:
            return json.dumps(body).encode() if body else None

    def _get_request_headers(self, files: Optional[Dict[str, BinaryIO]]) -> Dict[str, Any]:
        if files is not None and "Content-Type" in self._headers:
            return {key: value for key, value in self._headers.items() if key != "Content-Type"}

        return self._headers

    def add_headers(self, headers: Dict[str, Any]) -> None:
        self._headers.update(headers)

    @abstractmethod
    def execute_http_request(
        self,
        method: str,
        url: str,
        params: Optional[Dict] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
    ) -> httpx.Response:
        pass

    @abstractmethod
    def _request(
        self,
        files: Optional[Dict[str, BinaryIO]],
        method: str,
        params: Optional[Dict],
        body: Optional[Dict],
        url: str,
        stream: bool,
    ) -> httpx.Response:
        pass

    @abstractmethod
    def _init_client(self, client: Optional[_HttpxClientT]) -> _HttpxClientT:
        pass
