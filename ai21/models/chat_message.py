from dataclasses import dataclass
from typing import Optional

from ai21.models.role_type import RoleType
from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class ChatMessage(AI21BaseModelMixin):
    role: RoleType
    text: str
    name: Optional[str] = None
