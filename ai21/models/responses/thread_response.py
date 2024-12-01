from datetime import datetime
from typing import Optional, List, Literal

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.assistant.thread_message import ThreadMessageRole, ThreadMessageContentText


class ThreadMessage(AI21BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    object: Literal["message"] = "message"
    role: ThreadMessageRole
    content: ThreadMessageContentText
    run_id: Optional[str] = None
    assistant_id: Optional[str] = None


class Thread(AI21BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    object: Literal["thread"] = "thread"


class ListThread(AI21BaseModel):
    results: List[Thread]
