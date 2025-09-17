from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.maestro.run import Budget, ToolDefinition, ToolResources
from ai21.types import NOT_GIVEN, NotGiven


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
    description: Union[str, NotGiven] = NOT_GIVEN
    organization_id: str
    user_id: str
    models: List[str] | NotGiven = NOT_GIVEN
    tools: List[ToolDefinition] | NotGiven = NOT_GIVEN
    tool_resources: ToolResources | NotGiven = NOT_GIVEN
    requirements: List[Requirement] | NotGiven = NOT_GIVEN
    budget: Budget | NotGiven = NOT_GIVEN
    visibility: Visibility | NotGiven = NOT_GIVEN
    assistant_type: AgentType | NotGiven = NOT_GIVEN
    created_at: datetime
    updated_at: datetime
    response_language: ResponseLanguage | NotGiven = NOT_GIVEN


class ListAgentsResponse(AI21BaseModel):
    results: List[Agent]


class DeleteAgentResponse(AI21BaseModel):
    object: str = "agent"
    deleted: bool = True
    id: str
