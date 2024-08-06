from typing import Optional

from ai21.models import ChatMessage
from ai21.models.ai21_base_model import AI21BaseModel


class ConversationalRagSource(AI21BaseModel):
    text: str
    file_id: str
    file_name: str
    score: float
    order: Optional[int] = None
    public_url: Optional[str] = None
    labels: Optional[list[str]] = None


class ConversationalRagResponse(AI21BaseModel):
    id: str
    choices: list[ChatMessage]
    search_queries: Optional[list[str]]
    context_retrieved: bool
    answer_in_context: bool
    sources: list[ConversationalRagSource]
