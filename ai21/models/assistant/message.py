from __future__ import annotations
from typing import Literal, Union

from typing_extensions import TypedDict


ThreadMessageRole = Literal["assistant", "user"]


class ThreadMessageContentText(TypedDict):
    type: Literal["text"]
    text: str


ThreadMessageContent = Union[str, ThreadMessageContentText]


class Message(TypedDict):
    role: ThreadMessageRole
    content: ThreadMessageContent


def modify_message_content(message: Message) -> Message:
    role = message["role"]
    content = message["content"]

    if isinstance(content, str):
        content = ThreadMessageContentText(type="text", text=content)

    return Message(role=role, content=content)
