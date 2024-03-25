from dataclasses import dataclass

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin
from ai21.models.chat.role_type import RoleType


@dataclass
class ChatMessage(AI21BaseModelMixin):
    role: RoleType
    text: str
