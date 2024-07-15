from __future__ import annotations

from abc import ABC
from typing import Optional, Callable, Dict

from ai21.clients.studio.resources.studio_chat import StudioChat, AsyncStudioChat
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient

AzureADTokenProvider = Callable[[], str]
_DEFAULT_AZURE_VERSION = "v1"


class BaseAzureClient(ABC):
    _azure_endpoint: str
    _api_key: Optional[str]
    _azure_ad_token: Optional[str]
    _azure_ad_token_provider: Optional[AzureADTokenProvider]

    def _prepare_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        azure_ad_token = self._get_azure_ad_token()

        if azure_ad_token is not None and "Authorization" not in headers:
            return {
                "Authorization": f"Bearer {azure_ad_token}",
                **headers,
            }

        if self._api_key is not None:
            return {
                "api-key": self._api_key,
                **headers,
            }

        return headers

    def _get_azure_ad_token(self) -> Optional[str]:
        if self._azure_ad_token is not None:
            return self._azure_ad_token

        if self._azure_ad_token_provider is not None:
            return self._azure_ad_token_provider()

        return None

    def _add_version_to_url(self, base_url: str, api_version: str) -> str:
        if api_version:
            return f"{base_url}/{api_version}"

        return f"{base_url}/{_DEFAULT_AZURE_VERSION}"


class AsyncAI21AzureClient(BaseAzureClient, AsyncAI21HTTPClient):
    def __init__(
        self,
        base_url: str,
        api_version: str = _DEFAULT_AZURE_VERSION,
        api_key: Optional[str] = None,
        azure_ad_token: str | None = None,
        azure_ad_token_provider: AzureADTokenProvider | None = None,
        default_headers: Dict[str, str] | None = None,
        timeout_sec: int | None = None,
        num_retries: int | None = None,
    ):
        self._api_key = api_key
        self._azure_ad_token = azure_ad_token
        self._azure_ad_token_provider = azure_ad_token_provider

        if self._api_key is None and self._azure_ad_token_provider is None and self._azure_ad_token is None:
            raise ValueError("Must provide either api_key or azure_ad_token_provider or azure_ad_token")

        headers = self._prepare_headers(headers=default_headers or {})
        base_url = self._add_version_to_url(base_url=base_url, api_version=api_version)

        super().__init__(
            api_key=api_key,
            base_url=base_url,
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            requires_api_key=False,
        )

        self.chat = AsyncStudioChat(self)
        # Override the chat.create method to match the completions endpoint,
        # so it wouldn't get to the old J2 completion endpoint
        self.chat.create = self.chat.completions.create


class AI21AzureClient(BaseAzureClient, AI21HTTPClient):
    def __init__(
        self,
        base_url: str,
        api_version: str = _DEFAULT_AZURE_VERSION,
        api_key: Optional[str] = None,
        azure_ad_token: str | None = None,
        azure_ad_token_provider: AzureADTokenProvider | None = None,
        default_headers: Dict[str, str] | None = None,
        timeout_sec: int | None = None,
        num_retries: int | None = None,
    ):
        self._api_key = api_key
        self._azure_ad_token = azure_ad_token
        self._azure_ad_token_provider = azure_ad_token_provider

        if self._api_key is None and self._azure_ad_token_provider is None and self._azure_ad_token is None:
            raise ValueError("Must provide either api_key or azure_ad_token_provider or azure_ad_token")

        headers = self._prepare_headers(headers=default_headers or {})
        base_url = self._add_version_to_url(base_url=base_url, api_version=api_version)

        super().__init__(
            api_key=api_key,
            base_url=base_url,
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            requires_api_key=False,
        )

        self.chat = StudioChat(self)
        # Override the chat.create method to match the completions endpoint,
        # so it wouldn't get to the old J2 completion endpoint
        self.chat.create = self.chat.completions.create
