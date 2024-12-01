from typing import Literal

from typing_extensions import TypedDict

ThreadMessageRole = Literal["assistant", "user"]


class ThreadMessageContentText(TypedDict):
    type: Literal["text"]
    text: str


class CreateThreadMessagePayload(TypedDict):
    role: ThreadMessageRole
    content: ThreadMessageContentText
