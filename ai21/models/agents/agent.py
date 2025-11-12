from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

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


class AgentRequirement(AI21BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None


class Agent(AI21BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    organization_id: str
    user_id: str
    models: Optional[List[str]] = None
    tools: Optional[List[ToolDefinition]] = None
    tool_resources: Optional[ToolResources] = None
    requirements: Optional[List[AgentRequirement]] = None
    budget: Optional[Budget] = None
    visibility: Optional[Visibility] = None
    assistant_type: Optional[AgentType] = None
    created_at: datetime
    updated_at: datetime
    response_language: Optional[ResponseLanguage] = None


class ListAgentsResponse(AI21BaseModel):
    results: List[Agent]


class DeleteAgentResponse(AI21BaseModel):
    object: str = "agent"
    deleted: bool = True
    id: str
