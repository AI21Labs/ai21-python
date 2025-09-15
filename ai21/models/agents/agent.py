from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID

from ai21.models.ai21_base_model import AI21BaseModel


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


class Requirement(AI21BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None


class Agent(AI21BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    optimization: Optional[str] = None
    organization_id: str
    user_id: str
    avatar: Optional[str] = None
    is_archived: bool = False
    models: Optional[List[str]] = None
    tools: Optional[List[Dict[str, Any]]] = None
    tool_resources: Optional[Dict[str, Any]] = None
    requirements: Optional[List[Requirement]] = None
    budget: BudgetLevel = BudgetLevel.MEDIUM
    visibility: Visibility = Visibility.PUBLIC
    agent_type: AgentType = AgentType.DEFAULT
    created_at: datetime
    updated_at: datetime
    object: str = "agent"


class CreateAgentRequest(AI21BaseModel):
    name: str
    description: Optional[str] = None
    optimization: Optional[str] = None
    avatar: Optional[str] = None
    models: Optional[List[str]] = None
    tools: Optional[List[Dict[str, Any]]] = None
    tool_resources: Optional[Dict[str, Any]] = None
    requirements: Optional[List[Requirement]] = None
    budget: BudgetLevel = BudgetLevel.MEDIUM
    agent_type: Optional[AgentType] = AgentType.DEFAULT


class ModifyAgentRequest(AI21BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    optimization: Optional[str] = None
    avatar: Optional[str] = None
    is_archived: Optional[bool] = None
    models: Optional[List[str]] = None
    tools: Optional[List[Dict[str, Any]]] = None
    tool_resources: Optional[Dict[str, Any]] = None
    requirements: Optional[List[Requirement]] = None
    budget: Optional[BudgetLevel] = None
    visibility: Optional[Visibility] = None


class ListAgentsResponse(AI21BaseModel):
    results: List[Agent]


class DeleteAgentResponse(AI21BaseModel):
    object: str = "agent"
    deleted: bool = True
    id: str


class RunAgentRequest(AI21BaseModel):
    input: List[Dict[str, str]]  # Messages with role and content
    verbose: bool = False
    output_type: Optional[Dict[str, Any]] = None
    include: Optional[List[str]] = None
    structured_rag_enabled: bool = False
    dynamic_planning_enabled: bool = False
    response_language: str = "unset"


class RunResponse(AI21BaseModel):
    id: UUID
    status: str  # "completed", "failed", "in_progress", "requires_action"
    result: Optional[Any] = None
    data_sources: Optional[Dict[str, Any]] = None
    requirements_result: Optional[Dict[str, Any]] = None
