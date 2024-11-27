from datetime import datetime
from typing import Optional

from ai21.models.ai21_base_model import AI21BaseModel


class AssistantResponse(AI21BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    object: str
    name: str
    description: Optional[str]
    optimization: str
    organization_id: str
    user_id: str
    avatar: Optional[str] = None
    is_archived: bool = False
    models: Optional[list[str]] = None
    tools: Optional[list[str]] = None
    tool_resources: Optional[dict] = None
