from __future__ import annotations

from ai21.models.ai21_base_model import AI21BaseModel


class ChatMessage(AI21BaseModel):
    role: str
    content: str
