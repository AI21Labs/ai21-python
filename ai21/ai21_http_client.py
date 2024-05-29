import platform
from typing import Optional, Dict, Any, BinaryIO, TypeVar, Union

import httpx

from ai21.errors import MissingApiKeyError
from ai21.http_client import HttpClient, AsyncHttpClient
from ai21.version import VERSION

_HttpClientT = TypeVar("_HttpClientT", bound=Union[HttpClient, AsyncHttpClient])


class BaseAI21HTTPClient:
    _http_client: Optional[_HttpClientT] = None

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        requires_api_key: bool = True,
        api_host: Optional[str] = None,
        api_version: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[int] = None,
        num_retries: Optional[int] = None,
        via: Optional[str] = None,
    ):
        self._api_key = api_key

        if requires_api_key and not self._api_key:
            raise MissingApiKeyError()

        self._api_host = api_host
        self._api_version = api_version
        self._headers = headers
        self._timeout_sec = timeout_sec
        self._num_retries = num_retries
        self._via = via

        # headers = self._build_headers(passed_headers=headers)
        # self._http_client = self._init_http_client(http_client=http_client, headers=headers)

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

    def get_base_url(self) -> str:
        return f"{self._api_host}/studio/{self._api_version}"

    def _init_http_client(self, http_client: Optional[HttpClient], headers: Dict[str, Any]) -> _HttpClientT:
        raise NotImplementedError("Subclasses must implement this method")

    def execute_http_request(
        self,
        method: str,
        url: str,
        params: Optional[Dict] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
    ) -> httpx.Response:
        raise NotImplementedError("Subclasses must implement this method")


class AI21HTTPClient(BaseAI21HTTPClient):
    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        requires_api_key: bool = True,
        api_host: Optional[str] = None,
        api_version: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[int] = None,
        num_retries: Optional[int] = None,
        via: Optional[str] = None,
        http_client: Optional[HttpClient] = None,
    ):
        super().__init__(
            api_key=api_key,
            requires_api_key=requires_api_key,
            api_host=api_host,
            api_version=api_version,
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            via=via,
        )

        headers = self._build_headers(passed_headers=headers)
        self._http_client = self._init_http_client(http_client=http_client, headers=headers)

    def _init_http_client(self, http_client: Optional[HttpClient], headers: Dict[str, Any]) -> HttpClient:
        if http_client is None:
            return HttpClient(
                timeout_sec=self._timeout_sec,
                num_retries=self._num_retries,
                headers=headers,
            )

        http_client.add_headers(headers)

        return http_client

    def execute_http_request(
        self,
        method: str,
        url: str,
        params: Optional[Dict] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
    ) -> httpx.Response:
        return self._http_client.execute_http_request(
            method=method,
            url=url,
            params=params,
            files=files,
            stream=stream,
        )


class AsyncAI21HTTPClient(BaseAI21HTTPClient):
    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        requires_api_key: bool = True,
        api_host: Optional[str] = None,
        api_version: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[int] = None,
        num_retries: Optional[int] = None,
        via: Optional[str] = None,
        http_client: Optional[AsyncHttpClient] = None,
    ):
        super().__init__(
            api_key=api_key,
            requires_api_key=requires_api_key,
            api_host=api_host,
            api_version=api_version,
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            via=via,
        )

        headers = self._build_headers(passed_headers=headers)
        self._http_client = self._init_http_client(http_client=http_client, headers=self._headers)

    def _init_http_client(self, http_client: Optional[AsyncHttpClient], headers: Dict[str, Any]) -> AsyncHttpClient:
        if http_client is None:
            return AsyncHttpClient(
                timeout_sec=self._timeout_sec,
                num_retries=self._num_retries,
                headers=headers,
            )

        http_client.add_headers(headers)

        return http_client

    async def execute_http_request(
        self,
        method: str,
        url: str,
        params: Optional[Dict] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
    ) -> httpx.Response:
        return await self._http_client.execute_http_request(
            method=method,
            url=url,
            params=params,
            files=files,
            stream=stream,
        )
