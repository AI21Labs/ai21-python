from __future__ import annotations

from dataclasses import dataclass

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class ChatMessage(AI21BaseModelMixin):
    role: str
    content: str
