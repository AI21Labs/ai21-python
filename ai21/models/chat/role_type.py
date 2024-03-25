from enum import Enum

__all__ = ["RoleType"]


class RoleType(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
