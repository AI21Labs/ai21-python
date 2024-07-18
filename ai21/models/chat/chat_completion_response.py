from typing import Optional, List

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.logprobs import Logprobs
from ai21.models.usage_info import UsageInfo
from .chat_message import ChatMessage


class ChatCompletionResponseChoice(AI21BaseModel):
    index: int
    message: ChatMessage
    logprobs: Optional[Logprobs] = None
    finish_reason: Optional[str] = None


class ChatCompletionResponse(AI21BaseModel):
    id: str
    choices: List[ChatCompletionResponseChoice]
    usage: UsageInfo
