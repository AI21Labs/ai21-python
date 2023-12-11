from typing import Optional, List

from pydantic import BaseModel

from ai21.models.ai21_base_model import AI21BaseModel


class FinishReason(BaseModel):
    reason: str
    length: Optional[int] = None
    sequence: Optional[str] = None


class ChatOutput(AI21BaseModel):
    text: str
    role: str
    finish_reason: FinishReason


class ChatResponse(BaseModel):
    outputs: List[ChatOutput]
