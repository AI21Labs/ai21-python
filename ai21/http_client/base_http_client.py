from __future__ import annotations

import json
import platform
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Union, Any, Optional, Dict, BinaryIO

import httpx

from ai21.errors import (
    BadRequest,
    Unauthorized,
    UnprocessableEntity,
    TooManyRequestsError,
    AI21ServerError,
    ServiceUnavailable,
    AI21APIError,
    MissingApiKeyError,
)
from ai21.models.request_options import RequestOptions
from ai21.stream.async_stream import AsyncStream
from ai21.stream.stream import Stream
from ai21.version import VERSION

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
        base_url: str,
        api_key: Optional[str] = None,
        requires_api_key: bool = True,
        timeout_sec: int = None,
        num_retries: int = None,
        headers: Dict = None,
        via: Optional[str] = None,
    ):
        if requires_api_key and api_key is None:
            raise MissingApiKeyError()

        self._base_url = base_url
        self._api_key = api_key
        self._timeout_sec = timeout_sec or DEFAULT_TIMEOUT_SEC
        self._num_retries = num_retries or DEFAULT_NUM_RETRIES
        self._headers = headers or {}
        self._apply_retry_policy = self._num_retries > 0
        self._via = via

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

    def _get_request_headers(
        self, files: Optional[Dict[str, BinaryIO]], headers: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        if files is not None and "Content-Type" in self._headers:
            return {key: value for key, value in self._headers.items() if key != "Content-Type"}
        if headers is not None:
            return {**self._headers, **headers}
        return self._headers

    def add_headers(self, headers: Dict[str, Any]) -> None:
        self._headers.update(headers)

    @abstractmethod
    def execute_http_request(
        self,
        method: str,
        path: str,
        params: Optional[Dict] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
        extra_headers: Optional[Dict] = None,
    ) -> httpx.Response:
        pass

    @abstractmethod
    def _request(
        self,
        options: RequestOptions,
    ) -> httpx.Response:
        pass

    @abstractmethod
    def _init_client(self, client: Optional[_HttpxClientT]) -> _HttpxClientT:
        pass

    def _build_headers(self, passed_headers: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        headers = {
            "Content-Type": "application/json",
            "User-Agent": self._build_user_agent(),
        }

        if self._api_key:
            headers["Authorization"] = f"Bearer {self._api_key}"

        if passed_headers is not None:
            headers.update(passed_headers)

        return headers

    def _build_user_agent(self) -> str:
        user_agent = (
            f"AI21 studio SDK {VERSION} Python {platform.python_version()} Operating System {platform.platform()}"
        )

        if self._via is not None:
            user_agent = f"{user_agent} via: {self._via}"

        return user_agent

    def _build_request(self, options: RequestOptions) -> httpx.Request:
        data = self._get_request_data(files=options.files, method=options.method, body=options.body)
        headers = self._get_request_headers(files=options.files, headers=options.headers)

        return self._client.build_request(
            method=options.method,
            url=self._prepare_url(options),
            headers=headers,
            timeout=options.timeout,
            params=options.params,
            data=data,
            files=options.files,
        )

    def _prepare_url(self, options: RequestOptions) -> str:
        if options.path:
            return f"{options.url}{options.path}"

        return options.url
