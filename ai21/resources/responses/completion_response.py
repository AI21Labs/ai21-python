from typing import List, Optional, Union

from pydantic import BaseModel

from ai21.models.ai21_base_model import AI21BaseModel


class GeneratedToken(BaseModel):
    token: Optional[str]
    logprob: Optional[float]
    raw_logprob: Optional[float]


class TextRange(BaseModel):
    start: int
    end: int


class Token(AI21BaseModel):
    generated_token: Optional[GeneratedToken]
    top_tokens: Optional[List[GeneratedToken]]
    text_range: Optional[TextRange]


class Prompt(AI21BaseModel):
    text: Optional[str]
    tokens: Optional[List[Token]]


class CompletionData(AI21BaseModel):
    text: Optional[str]
    tokens: Optional[List[Token]]


class CompletionFinishReason(AI21BaseModel):
    reason: Optional[str] = None
    length: Optional[int] = None


class Completion(AI21BaseModel):
    data: CompletionData
    finish_reason: CompletionFinishReason


class CompletionsResponse(AI21BaseModel):
    id: Union[int, str]
    prompt: Prompt
    completions: List[Completion]
