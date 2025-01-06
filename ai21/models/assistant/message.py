from typing import Literal, Union

from typing_extensions import TypedDict


ThreadMessageRole = Literal["assistant", "user"]


class MessageContentText(TypedDict):
    type: Literal["text"]
    text: str


class Message(TypedDict):
    role: ThreadMessageRole
    content: Union[str, MessageContentText]


def modify_message_content(message: Message) -> Message:
    role = message["role"]
    content = message["content"]

    if isinstance(content, str):
        content = MessageContentText(type="text", text=content)

    return Message(role=role, content=content)
