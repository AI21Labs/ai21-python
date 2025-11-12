from typing import Any, Dict, Optional

import httpx

from ai21.ai21_env_config import AI21EnvConfig, _AI21EnvConfig
from ai21.clients.studio.resources.beta.beta import Beta
from ai21.clients.studio.resources.studio_chat import StudioChat
from ai21.clients.studio.resources.studio_library import StudioLibrary
from ai21.http_client.http_client import AI21HTTPClient


class AI21Client(AI21HTTPClient):
    """
    This class would be sending requests to our REST API using http requests
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_host: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        via: Optional[str] = None,
        http_client: Optional[httpx.Client] = None,
        env_config: _AI21EnvConfig = AI21EnvConfig,
        **kwargs,
    ):
        base_url = api_host or env_config.api_host
        super().__init__(
            api_key=api_key or env_config.api_key,
            base_url=base_url,
            headers=headers,
            timeout_sec=timeout_sec or env_config.timeout_sec,
            num_retries=num_retries or env_config.num_retries,
            via=via,
            client=http_client,
        )
        self.chat: StudioChat = StudioChat(self)
        self.library = StudioLibrary(self)
        self.beta = Beta(self)
