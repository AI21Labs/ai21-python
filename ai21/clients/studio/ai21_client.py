import warnings
from typing import Optional, Any, Dict

from ai21_tokenizer import PreTrainedTokenizers

from ai21.ai21_env_config import _AI21EnvConfig, AI21EnvConfig
from ai21.ai21_http_client import AI21HTTPClient, AsyncAI21HTTPClient
from ai21.clients.studio.resources.beta.beta import Beta, AsyncBeta
from ai21.clients.studio.resources.studio_answer import StudioAnswer, AsyncStudioAnswer
from ai21.clients.studio.resources.studio_chat import StudioChat, AsyncStudioChat
from ai21.clients.studio.resources.studio_completion import StudioCompletion, AsyncStudioCompletion
from ai21.clients.studio.resources.studio_custom_model import StudioCustomModel, AsyncStudioCustomModel
from ai21.clients.studio.resources.studio_dataset import StudioDataset, AsyncStudioDataset
from ai21.clients.studio.resources.studio_embed import StudioEmbed, AsyncStudioEmbed
from ai21.clients.studio.resources.studio_gec import StudioGEC, AsyncStudioGEC
from ai21.clients.studio.resources.studio_improvements import StudioImprovements, AsyncStudioImprovements
from ai21.clients.studio.resources.studio_library import StudioLibrary, AsyncStudioLibrary
from ai21.clients.studio.resources.studio_paraphrase import StudioParaphrase, AsyncStudioParaphrase
from ai21.clients.studio.resources.studio_segmentation import StudioSegmentation, AsyncStudioSegmentation
from ai21.clients.studio.resources.studio_summarize import StudioSummarize, AsyncStudioSummarize
from ai21.clients.studio.resources.studio_summarize_by_segment import (
    StudioSummarizeBySegment,
    AsyncStudioSummarizeBySegment,
)
from ai21.http_client import HttpClient, AsyncHttpClient
from ai21.tokenizers.ai21_tokenizer import AI21Tokenizer
from ai21.tokenizers.factory import get_tokenizer


class AI21Client:
    """
    This class would be sending requests to our REST API using http requests
    """

    _tokenizer: Optional[AI21Tokenizer]

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_host: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        via: Optional[str] = None,
        http_client: Optional[HttpClient] = None,
        env_config: _AI21EnvConfig = AI21EnvConfig,
        **kwargs,
    ):
        self._http_client = AI21HTTPClient(
            api_key=api_key or env_config.api_key,
            api_host=api_host or env_config.api_host,
            api_version=env_config.api_version,
            headers=headers,
            timeout_sec=timeout_sec or env_config.timeout_sec,
            num_retries=num_retries or env_config.num_retries,
            via=via,
            http_client=http_client,
        )
        self.completion = StudioCompletion(self._http_client)
        self.chat: StudioChat = StudioChat(self._http_client)
        self.summarize = StudioSummarize(self._http_client)
        self.embed = StudioEmbed(self._http_client)
        self.gec = StudioGEC(self._http_client)
        self.improvements = StudioImprovements(self._http_client)
        self.paraphrase = StudioParaphrase(self._http_client)
        self.summarize_by_segment = StudioSummarizeBySegment(self._http_client)
        self.custom_model = StudioCustomModel(self._http_client)
        self.dataset = StudioDataset(self._http_client)
        self.answer = StudioAnswer(self._http_client)
        self.library = StudioLibrary(self._http_client)
        self.segmentation = StudioSegmentation(self._http_client)
        self.beta = Beta(self._http_client)

    def count_tokens(self, text: str, tokenizer_name: str = PreTrainedTokenizers.J2_TOKENIZER) -> int:
        warnings.warn(
            "Please use the global get_tokenizer() method directly instead of the AI21Client().count_tokens() method.",
            DeprecationWarning,
        )

        tokenizer = get_tokenizer(tokenizer_name)
        return tokenizer.count_tokens(text)


class AsyncAI21Client:
    """
    This class would be sending requests to our REST API using http requests asynchronously
    """

    # TODO: Use async tokenizer
    _tokenizer: Optional[AI21Tokenizer]

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
        self._http_client = AsyncAI21HTTPClient(
            api_key=api_key or env_config.api_key,
            api_host=api_host or env_config.api_host,
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
