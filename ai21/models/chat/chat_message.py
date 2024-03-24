from dataclasses import dataclass

from ai21.models import RoleType
from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class ChatMessage(AI21BaseModelMixin):
    role: RoleType
    content: str
