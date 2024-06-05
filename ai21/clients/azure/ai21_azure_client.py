from __future__ import annotations

from typing import Optional, Callable, Dict

from ai21.ai21_http_client import AI21HTTPClient
from ai21.clients.studio.resources.studio_chat import StudioChat

AzureADTokenProvider = Callable[[], str]


class AI21AzureClient(AI21HTTPClient):
    def __init__(
        self,
        azure_endpoint: str,
        api_version: Optional[str] = None,
        api_key: Optional[str] = None,
        azure_ad_token_provider: AzureADTokenProvider | None = None,
        default_headers: Dict[str, str] | None = None,
        timeout_sec: Optional[int] = None,
    ):
        self._api_key = api_key
        self._azure_ad_token_provider = azure_ad_token_provider

        headers = self._prepare_headers(headers=default_headers or {})
        super().__init__(
            api_key=api_key,
            api_version=api_version,
            api_host=f"{azure_endpoint}/openai",
            headers=headers,
            timeout_sec=timeout_sec,
        )

        self.chat: StudioChat = StudioChat(self)

    def _prepare_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        if "Authorization" not in headers:
            if self._api_key is not None:
                headers["api-key"] = self._api_key
            elif self._azure_ad_token_provider is not None:
                headers["Authorization"] = f"Bearer {self._azure_ad_token_provider()}"
            else:
                raise ValueError("Either api_key or azure token")

        return headers

    def get_base_url(self) -> str:
        return self._api_host + "/deployments/{model_name}/chat/completions?api-version=" + self._api_version
