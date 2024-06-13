import platform
from typing import Optional, Dict, Any, BinaryIO, TypeVar, Union
from abc import ABC, abstractmethod

import httpx

from ai21.errors import MissingApiKeyError
from ai21.http_client.http_client import HttpClient
from ai21.http_client.async_http_client import AsyncHttpClient
from ai21.version import VERSION


_HttpClientT = TypeVar("_HttpClientT", bound=Union[HttpClient, AsyncHttpClient])


class BaseAI21HTTPClient(ABC):
    _http_client: Optional[_HttpClientT] = None

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        requires_api_key: bool = True,
        base_url: Optional[str] = None,
        api_version: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[int] = None,
        num_retries: Optional[int] = None,
        via: Optional[str] = None,
    ):
        self._api_key = api_key

        if requires_api_key and not self._api_key:
            raise MissingApiKeyError()

        self._base_url = base_url
        self._api_version = api_version
        self._headers = headers
        self._timeout_sec = timeout_sec
        self._num_retries = num_retries
        self._via = via

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

    @abstractmethod
    def _init_http_client(self, http_client: Optional[HttpClient], headers: Dict[str, Any]) -> _HttpClientT:
        pass

    @abstractmethod
    def execute_http_request(
        self,
        method: str,
        path: str,
        params: Optional[Dict] = None,
        body: Optional[Dict] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
    ) -> httpx.Response:
        pass
