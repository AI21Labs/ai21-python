from typing import Optional, List

from pydantic import Field

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.chat.role_type import RoleType


class FinishReason(AI21BaseModel):
    reason: str
    length: Optional[int] = None
    sequence: Optional[str] = None


class ChatOutput(AI21BaseModel):
    text: str
    role: RoleType
    finish_reason: Optional[FinishReason] = Field(default=None, alias="finishReason")


class ChatResponse(AI21BaseModel):
    outputs: List[ChatOutput]
