from dataclasses import dataclass
from typing import Optional, List

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin
from ai21.models.logprobs import Logprobs
from ai21.models.usage_info import UsageInfo


@dataclass
class ChoiceDelta(AI21BaseModelMixin):
    content: Optional[str] = None
    role: Optional[str] = None


@dataclass
class ChoicesChunk(AI21BaseModelMixin):
    index: int
    delta: ChoiceDelta
    logprobs: Optional[Logprobs] = None
    finish_reason: Optional[str] = None


@dataclass
class ChatCompletionChunk(AI21BaseModelMixin):
    id: str
    choices: List[ChoicesChunk]
    usage: Optional[UsageInfo] = None
