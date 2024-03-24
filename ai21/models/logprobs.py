from dataclasses import dataclass
from typing import List

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class TopTokenData(AI21BaseModelMixin):
    token: str
    logprob: float


@dataclass
class LogprobsData(AI21BaseModelMixin):
    token: str
    logprob: float
    top_logprobs: List[TopTokenData]


@dataclass
class Logprobs(AI21BaseModelMixin):
    content: LogprobsData
