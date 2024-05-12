from dataclasses import dataclass
from typing import Optional, List

from ai21.models.logprobs import Logprobs
from ai21.models.usage_info import UsageInfo


@dataclass
class ChoicesChunk:
    index: int
    delta: dict
    logprobs: Optional[Logprobs] = None
    finish_reason: Optional[str] = None


@dataclass
class ChatCompletionChunk:
    id: str
    choices: List[ChoicesChunk]
    usage: Optional[UsageInfo] = None
