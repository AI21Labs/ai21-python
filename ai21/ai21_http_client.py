from typing import Optional, Dict, Any, BinaryIO

from ai21.ai21_env_config import _AI21EnvConfig, AI21EnvConfig
from ai21.errors import MissingApiKeyError
from ai21.http_client import HttpClient
from ai21.version import VERSION


class AI21HTTPClient:
    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        api_host: Optional[str] = None,
        api_version: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[int] = None,
        num_retries: Optional[int] = None,
        organization: Optional[str] = None,
        application: Optional[str] = None,
        via: Optional[str] = None,
        http_client: Optional[HttpClient] = None,
        env_config: _AI21EnvConfig = AI21EnvConfig,
    ):
        self._env_config = env_config
        self._api_key = api_key or self._env_config.api_key

        if self._api_key is None:
            raise MissingApiKeyError()

        self._api_host = api_host or self._env_config.api_host
        self._api_version = api_version or self._env_config.api_version
        self._headers = headers
        self._timeout_sec = timeout_sec or self._env_config.timeout_sec
        self._num_retries = num_retries or self._env_config.num_retries
        self._organization = organization
        self._application = application
        self._via = via

        headers = self._build_headers(passed_headers=headers)
        self._http_client = self._init_http_client(http_client=http_client, headers=headers)

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

    def _init_http_client(self, http_client: Optional[HttpClient], headers: Dict[str, Any]) -> HttpClient:
        if http_client is None:
            return HttpClient(
                timeout_sec=self._timeout_sec,
                num_retries=self._num_retries,
                headers=headers,
            )

        http_client.add_headers(headers)

        return http_client

    def _build_user_agent(self) -> str:
        user_agent = f"ai21 studio SDK {VERSION}"

        if self._organization is not None:
            user_agent = f"{user_agent} organization: {self._organization}"

        if self._application is not None:
            user_agent = f"{user_agent} application: {self._application}"

        if self._via is not None:
            user_agent = f"{user_agent} via: {self._via}"

        return user_agent

    def execute_http_request(
        self,
        method: str,
        url: str,
        params: Optional[Dict] = None,
        files: Optional[Dict[str, BinaryIO]] = None,
    ):
        return self._http_client.execute_http_request(method=method, url=url, params=params, files=files)

    def get_base_url(self) -> str:
        return f"{self._api_host}/studio/{self._api_version}"
