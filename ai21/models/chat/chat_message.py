from __future__ import annotations
from typing_extensions import TypedDict, Literal


class ChatMessage(TypedDict):
    role: str | Literal["user", "assistant", "system"]
    content: str
