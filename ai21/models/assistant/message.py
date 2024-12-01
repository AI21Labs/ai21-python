from datetime import datetime
from typing import Literal, Optional

from typing_extensions import TypedDict

from ai21.models.ai21_base_model import AI21BaseModel

ThreadMessageRole = Literal["assistant", "user"]


class MessageContentText(TypedDict):
    type: Literal["text"]
    text: str


class Message(TypedDict):
    role: ThreadMessageRole
    content: MessageContentText


class MessageResponse(AI21BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    object: Literal["message"] = "message"
    role: ThreadMessageRole
    content: MessageContentText
    run_id: Optional[str] = None
    assistant_id: Optional[str] = None
