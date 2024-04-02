from __future__ import annotations

from typing_extensions import TypedDict, Literal


class ChatMessage(TypedDict):
    role: Literal["user", "assistant"]
    content: str
