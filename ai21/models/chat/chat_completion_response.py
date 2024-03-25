from dataclasses import dataclass
from typing import Optional, List

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin
from ai21.models.chat import ChatMessage
from ai21.models.logprobs import Logprobs
from ai21.models.usage_info import UsageInfo

__all__ = ["ChatCompletionResponse", "ChatCompletionResponseChoice"]


@dataclass
class ChatCompletionResponseChoice(AI21BaseModelMixin):
    index: int
    message: ChatMessage
    logprobs: Optional[Logprobs] = None
    finish_reason: Optional[str] = None


@dataclass
class ChatCompletionResponse(AI21BaseModelMixin):
    id: str
    choices: List[ChatCompletionResponseChoice]
    usage: UsageInfo
