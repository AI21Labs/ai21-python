from datetime import datetime
from typing import Literal, Optional, List

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.assistant.message import ThreadMessageRole, MessageContentText


class MessageResponse(AI21BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    object: Literal["message"] = "message"
    role: ThreadMessageRole
    content: MessageContentText
    run_id: Optional[str] = None
    assistant_id: Optional[str] = None


class ListMessageResponse(AI21BaseModel):
    results: List[MessageResponse]
