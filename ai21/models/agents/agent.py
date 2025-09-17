from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.maestro.run import Budget, ToolDefinition, ToolResources


class BudgetLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Visibility(str, Enum):
    PUBLIC = "public"
    PRIVATE = "private"


class AgentType(str, Enum):
    DEFAULT = "default"
    CHAT = "chat"
    MAESTRO = "maestro"
    RAG = "rag"


class ResponseLanguage(str, Enum):
    ARABIC = "arabic"
    DUTCH = "dutch"
    ENGLISH = "english"
    FRENCH = "french"
    GERMAN = "german"
    HEBREW = "hebrew"
    ITALIAN = "italian"
    PORTUGUESE = "portuguese"
    SPANISH = "spanish"
    UNSET = "unset"


class Requirement(AI21BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None


class Agent(AI21BaseModel):
    id: str
    name: str
    description: Union[str, None] = None
    organization_id: str
    user_id: str
    models: Union[List[str], None] = None
    tools: Union[List[ToolDefinition], None] = None
    tool_resources: Union[ToolResources, None] = None
    requirements: Union[List[Requirement], None] = None
    budget: Union[Budget, None] = None
    visibility: Union[Visibility, None] = None
    assistant_type: Union[AgentType, None] = None
    created_at: datetime
    updated_at: datetime
    response_language: Union[ResponseLanguage, None] = None


class ListAgentsResponse(AI21BaseModel):
    results: List[Agent]


class DeleteAgentResponse(AI21BaseModel):
    object: str = "agent"
    deleted: bool = True
    id: str
