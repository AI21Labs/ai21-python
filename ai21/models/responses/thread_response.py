from datetime import datetime
from typing import List, Literal

from ai21.models.ai21_base_model import AI21BaseModel


class ThreadResponse(AI21BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    object: Literal["thread"] = "thread"


class ListThread(AI21BaseModel):
    results: List[ThreadResponse]
