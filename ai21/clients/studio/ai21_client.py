from typing import Optional, Any, Dict

from ai21.ai21_studio_client import AI21StudioClient
from ai21.clients.studio.resources.studio_answer import StudioAnswer
from ai21.clients.studio.resources.studio_chat import StudioChat
from ai21.clients.studio.resources.studio_completion import StudioCompletion
from ai21.clients.studio.resources.studio_custom_model import StudioCustomModel
from ai21.clients.studio.resources.studio_dataset import StudioDataset
from ai21.clients.studio.resources.studio_embed import StudioEmbed
from ai21.clients.studio.resources.studio_gec import StudioGEC
from ai21.clients.studio.resources.studio_improvements import StudioImprovements
from ai21.clients.studio.resources.studio_library import StudioLibrary
from ai21.clients.studio.resources.studio_paraphrase import StudioParaphrase
from ai21.clients.studio.resources.studio_segmentation import StudioSegmentation
from ai21.clients.studio.resources.studio_summarize import StudioSummarize
from ai21.clients.studio.resources.studio_summarize_by_segment import StudioSummarizeBySegment
from ai21.tokenizers.ai21_tokenizer import AI21Tokenizer
from ai21.tokenizers.factory import get_tokenizer


class AI21Client:
    """
    These class would be sending requests to our REST API using http requests
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
        **kwargs,
    ):
        self._studio_client = AI21StudioClient(
            api_key=api_key,
            api_host=api_host,
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            via=via,
        )
        self.completion = StudioCompletion(self._studio_client)
        self.chat = StudioChat(self._studio_client)
        self.summarize = StudioSummarize(self._studio_client)
        self.embed = StudioEmbed(self._studio_client)
        self.gec = StudioGEC(self._studio_client)
        self.improvements = StudioImprovements(self._studio_client)
        self.paraphrase = StudioParaphrase(self._studio_client)
        self.summarize_by_segment = StudioSummarizeBySegment(self._studio_client)
        self.custom_model = StudioCustomModel(self._studio_client)
        self.dataset = StudioDataset(self._studio_client)
        self.answer = StudioAnswer(self._studio_client)
        self.library = StudioLibrary(self._studio_clienself._studio_clientt)
        self.segmentation = StudioSegmentation()

    def count_tokens(self, text: str) -> int:
        # We might want to cache the tokenizer instance within the class
        # and not globally as it might be used by other instances

        tokenizer = get_tokenizer()
        return tokenizer.count_tokens(text)
