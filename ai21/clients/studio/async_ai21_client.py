from typing import Optional, Any, Dict

import httpx

from ai21.ai21_env_config import _AI21EnvConfig, AI21EnvConfig
from ai21.clients.studio.client_url_parser import create_client_url
from ai21.clients.studio.resources.beta.async_beta import AsyncBeta
from ai21.clients.studio.resources.studio_chat import AsyncStudioChat
from ai21.clients.studio.resources.studio_library import AsyncStudioLibrary
from ai21.http_client.async_http_client import AsyncAI21HTTPClient


class AsyncAI21Client(AsyncAI21HTTPClient):
    """
    This class would be sending requests to our REST API using http requests asynchronously
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_host: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        via: Optional[str] = None,
        http_client: Optional[httpx.AsyncClient] = None,
        env_config: _AI21EnvConfig = AI21EnvConfig,
        **kwargs,
    ):
        base_url = create_client_url(api_host or env_config.api_host)

        super().__init__(
            api_key=api_key or env_config.api_key,
            base_url=base_url,
            headers=headers,
            timeout_sec=timeout_sec or env_config.timeout_sec,
            num_retries=num_retries or env_config.num_retries,
            via=via,
            client=http_client,
        )

        self.chat: AsyncStudioChat = AsyncStudioChat(self)
        self.library = AsyncStudioLibrary(self)
        self.beta = AsyncBeta(self)
