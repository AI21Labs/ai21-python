from __future__ import annotations
from typing import Optional, List

from ai21.models.chat import ChatMessage
from ai21.models.ai21_base_model import AI21BaseModel


class ConversationalRagSource(AI21BaseModel):
    text: str
    file_id: str
    file_name: str
    score: float
    order: Optional[int] = None
    public_url: Optional[str] = None
    labels: Optional[List[str]] = None


class ConversationalRagResponse(AI21BaseModel):
    id: str
    choices: List[ChatMessage]
    search_queries: Optional[List[str]]
    context_retrieved: bool
    answer_in_context: bool
    sources: List[ConversationalRagSource]
