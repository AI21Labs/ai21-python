from typing import Optional, Any, Dict

from ai21.ai21_env_config import _AI21EnvConfig, AI21EnvConfig
from ai21.ai21_http_client.async_ai21_http_client import AsyncAI21HTTPClient
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
from ai21.http_client.async_http_client import AsyncHttpClient


class AsyncAI21Client:
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
        http_client: Optional[AsyncHttpClient] = None,
        env_config: _AI21EnvConfig = AI21EnvConfig,
        **kwargs,
    ):
        base_url = create_client_url(api_host or env_config.api_host)

        self._http_client = AsyncAI21HTTPClient(
            api_key=api_key or env_config.api_key,
            base_url=base_url,
            api_version=env_config.api_version,
            headers=headers,
            timeout_sec=timeout_sec or env_config.timeout_sec,
            num_retries=num_retries or env_config.num_retries,
            via=via,
            http_client=http_client,
        )

        self.completion = AsyncStudioCompletion(self._http_client)
        self.chat: AsyncStudioChat = AsyncStudioChat(self._http_client)
        self.summarize = AsyncStudioSummarize(self._http_client)
        self.embed = AsyncStudioEmbed(self._http_client)
        self.gec = AsyncStudioGEC(self._http_client)
        self.improvements = AsyncStudioImprovements(self._http_client)
        self.paraphrase = AsyncStudioParaphrase(self._http_client)
        self.summarize_by_segment = AsyncStudioSummarizeBySegment(self._http_client)
        self.custom_model = AsyncStudioCustomModel(self._http_client)
        self.dataset = AsyncStudioDataset(self._http_client)
        self.answer = AsyncStudioAnswer(self._http_client)
        self.library = AsyncStudioLibrary(self._http_client)
        self.segmentation = AsyncStudioSegmentation(self._http_client)
        self.beta = AsyncBeta(self._http_client)
