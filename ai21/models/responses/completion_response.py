from typing import List, Optional, Union, Any, Dict

from pydantic import Field

from ai21.models.ai21_base_model import AI21BaseModel


class Prompt(AI21BaseModel):
    text: Optional[str]
    tokens: Optional[List[Dict[str, Any]]] = None


class CompletionData(AI21BaseModel):
    text: Optional[str]
    tokens: Optional[List[Dict[str, Any]]] = None


class CompletionFinishReason(AI21BaseModel):
    reason: Optional[str] = None
    length: Optional[int] = None


class Completion(AI21BaseModel):
    data: CompletionData
    finish_reason: Optional[CompletionFinishReason] = Field(default=None, alias="finishReason")


class CompletionsResponse(AI21BaseModel):
    id: Union[int, str]
    prompt: Prompt
    completions: List[Completion]
