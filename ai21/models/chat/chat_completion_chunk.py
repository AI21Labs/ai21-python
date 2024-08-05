from typing import Optional, List

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.logprobs import Logprobs
from ai21.models.usage_info import UsageInfo


class ChoiceDelta(AI21BaseModel):
    content: Optional[str] = None
    role: Optional[str] = None


class ChoicesChunk(AI21BaseModel):
    index: int
    delta: ChoiceDelta
    logprobs: Optional[Logprobs] = None
    finish_reason: Optional[str] = None


class ChatCompletionChunk(AI21BaseModel):
    id: str
    choices: List[ChoicesChunk]
    usage: Optional[UsageInfo] = None
