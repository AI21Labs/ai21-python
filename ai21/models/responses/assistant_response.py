from datetime import datetime
from typing import Optional, List, Literal

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.assistant.assistant import ToolResources


class AssistantResponse(AI21BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    object: Literal["assistant"] = "assistant"
    name: str
    description: Optional[str] = None
    optimization: str
    organization_id: str
    user_id: str
    avatar: Optional[str] = None
    is_archived: bool = False
    models: Optional[List[str]] = None
    tools: Optional[List[str]] = None
    tool_resources: Optional[ToolResources] = None


class ListAssistant(AI21BaseModel):
    results: List[AssistantResponse]


class DeletedAssistantResponse(AI21BaseModel):
    object: Literal["assistant"] = "assistant"
    deleted: bool = True
    id: str
