from datetime import datetime
from typing import Optional, List, Literal

from typing_extensions import TypedDict

from ai21.models.ai21_base_model import AI21BaseModel


MessageRole = Literal["assistant", "user"]


class MessageContentText(TypedDict):
    type: Literal["text"]
    text: str


class CreateMessagePayload(TypedDict):
    role: MessageRole
    content: MessageContentText


class ThreadMessageResponse(AI21BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    object: Literal["message"] = "message"
    role: MessageRole
    content: MessageContentText
    run_id: Optional[str] = None
    assistant_id: Optional[str] = None


class ThreadResponse(AI21BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    object: Literal["thread"] = "thread"


class ListThreadResponse(AI21BaseModel):
    results: List[ThreadResponse]
