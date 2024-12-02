from typing import Literal

from typing_extensions import TypedDict

ThreadMessageRole = Literal["assistant", "user"]


class MessageContentText(TypedDict):
    type: Literal["text"]
    text: str


class Message(TypedDict):
    role: ThreadMessageRole
    content: MessageContentText
