from __future__ import annotations

from typing_extensions import TypedDict, Literal

from .role_type import RoleType


class ChatMessage(TypedDict):
    role: RoleType | Literal["user", "assistant"]
    content: str
