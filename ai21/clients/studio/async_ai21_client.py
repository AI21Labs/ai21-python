from typing import Optional, Any, Dict

import httpx

from ai21.ai21_env_config import _AI21EnvConfig, AI21EnvConfig
from ai21.clients.studio.client_url_parser import create_client_url
from ai21.clients.studio.resources.beta.async_beta import AsyncBeta
from ai21.clients.studio.resources.studio_answer import AsyncStudioAnswer
from ai21.clients.studio.resources.studio_chat import AsyncStudioChat
from ai21.clients.studio.resources.studio_completion import AsyncStudioCompletion
from ai21.clients.studio.resources.studio_custom_model import AsyncStudioCustomModel
from ai21.clients.studio.resources.studio_dataset import AsyncStudioDataset
from ai21.clients.studio.resources.studio_embed import AsyncStudioEmbed
from ai21.clients.studio.resources.studio_gec import AsyncStudioGEC
from ai21.clients.studio.resources.studio_improvements import AsyncStudioImprovements
from ai21.clients.studio.resources.studio_library import AsyncStudioLibrary
from ai21.clients.studio.resources.studio_paraphrase import AsyncStudioParaphrase
from ai21.clients.studio.resources.studio_segmentation import AsyncStudioSegmentation
from ai21.clients.studio.resources.studio_summarize import AsyncStudioSummarize
from ai21.clients.studio.resources.studio_summarize_by_segment import AsyncStudioSummarizeBySegment
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

        self.completion = AsyncStudioCompletion(self)
        self.chat: AsyncStudioChat = AsyncStudioChat(self)
        self.summarize = AsyncStudioSummarize(self)
        self.embed = AsyncStudioEmbed(self)
        self.gec = AsyncStudioGEC(self)
        self.improvements = AsyncStudioImprovements(self)
        self.paraphrase = AsyncStudioParaphrase(self)
        self.summarize_by_segment = AsyncStudioSummarizeBySegment(self)
        self.custom_model = AsyncStudioCustomModel(self)
        self.dataset = AsyncStudioDataset(self)
        self.answer = AsyncStudioAnswer(self)
        self.library = AsyncStudioLibrary(self)
        self.segmentation = AsyncStudioSegmentation(self)
        self.beta = AsyncBeta(self)
