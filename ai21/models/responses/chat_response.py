from dataclasses import dataclass
from typing import Optional, List

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin
from ai21.models.chat.role_type import RoleType


@dataclass
class FinishReason(AI21BaseModelMixin):
    reason: str
    length: Optional[int] = None
    sequence: Optional[str] = None


@dataclass
class ChatOutput(AI21BaseModelMixin):
    text: str
    role: RoleType
    finish_reason: FinishReason


@dataclass
class ChatResponse(AI21BaseModelMixin):
    outputs: List[ChatOutput]
