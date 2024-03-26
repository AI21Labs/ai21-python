from enum import Enum


class RoleType(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
