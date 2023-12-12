from typing import Optional, Any, Dict

from ai21.ai21_studio_client import AI21StudioClient
from ai21.clients.studio import resources
from ai21.tokenizers.ai21_tokenizer import AI21Tokenizer
from ai21.tokenizers.factory import get_tokenizer

__all__ = ["AI21Client", "resources"]


class AI21Client(AI21StudioClient):
    """
    These class would be sending requests to our REST API using http requests
    """

    _tokenizer: Optional[AI21Tokenizer]

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_host: Optional[str] = None,
        auth_required: bool = True,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        **kwargs,
    ):
        super().__init__(
            api_key=api_key,
            api_host=api_host,
            auth_required=auth_required,
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
        )
        self.completion = resources.StudioCompletion(self)
        self.chat = resources.StudioChat(self)
        self.summarize = resources.StudioSummarize(self)
        self.embed = resources.StudioEmbed(self)
        self.gec = resources.StudioGEC(self)
        self.improvements = resources.StudioImprovements(self)
        self.paraphrase = resources.StudioParaphrase(self)
        self.summarize_by_segment = resources.StudioSummarizeBySegment(self)
        self.custom_model = resources.StudioCustomModel(self)
        self.dataset = resources.StudioDataset(self)
        self.answer = resources.StudioAnswer(self)
        self.library = resources.StudioLibrary(self)
        self.segmentation = resources.StudioSegmentation(self)

    def count_token(self, text: str, model_id: str = "j2-instruct") -> int:
        # We might want to cache the tokenizer instance within the class
        # and not globally as it might be used by other instances

        tokenizer = get_tokenizer()
        return tokenizer.count_tokens(text)
