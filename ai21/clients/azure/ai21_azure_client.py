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

        # TODO: Change - The "/openai" suffix will probably change to "/ai21" once we have a working endpoint in Azure.
        super().__init__(
            api_key=api_key,
            api_version=api_version,
            api_host=f"{azure_endpoint}/openai",
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
        )

        self.chat = StudioChat(self)
        # Override the chat.create method to match the completions endpoint,
        # so it wouldn't get to the old J2 completion endpoint
        self.chat.create = self.chat.completions.create

    def _prepare_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        azure_ad_token = self._get_azure_ad_token()

        if azure_ad_token is not None and "Authorization" not in headers:
            return headers.update({"Authorization": f"Bearer {azure_ad_token}"}) or headers

        if self._api_key is not None:
            return headers.update({"api-key": self._api_key}) or headers

        return headers

    def _get_azure_ad_token(self) -> Optional[str]:
        if self._azure_ad_token is not None:
            return self._azure_ad_token

        if self._azure_ad_token_provider is not None:
            return self._azure_ad_token_provider()

        return None

    def get_base_url(self, module_name: str, model: Optional[str] = None) -> str:
        base_url = self._api_host + "/deployments"

        if model is not None:
            base_url += f"/{model}"

        base_url += f"/{module_name}"

        if self._api_version is None:
            return base_url

        return f"{base_url}?api-version={self._api_version}"
