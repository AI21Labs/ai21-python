from typing_extensions import TypedDict


class ChatMessage(TypedDict):
    role: str
    content: str
