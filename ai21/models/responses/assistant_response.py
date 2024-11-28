from datetime import datetime
from typing import Optional, List, Literal, TypedDict

from ai21.models.ai21_base_model import AI21BaseModel


Optimization = Literal["cost", "latency"]
Model = Literal["jamba-1-5", "jamba-1-5-large"]
Tool = Literal["rag", "internet_research", "plan_approval"]


class ToolsResources(TypedDict, total=False):
    rag: Optional[dict]
    internet_research: Optional[dict]
    plan_approval: Optional[dict]


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
    models: Optional[List[str]] = None
    tools: Optional[List[str]] = None
    tool_resources: Optional[dict] = None
