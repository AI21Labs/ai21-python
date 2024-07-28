from typing import List

from ai21.models.ai21_base_model import AI21BaseModel


class TopTokenData(AI21BaseModel):
    token: str
    logprob: float


class LogprobsData(AI21BaseModel):
    token: str
    logprob: float
    top_logprobs: List[TopTokenData]


class Logprobs(AI21BaseModel):
    content: LogprobsData
