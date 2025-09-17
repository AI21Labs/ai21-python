from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Dict, Any

from ai21.models.agents import (
    Agent,
    AgentType,
    BudgetLevel,
    DeleteAgentResponse,
    ListAgentsResponse,
    Requirement,
    Visibility,
)
from ai21.models.agents.agent import ResponseLanguage
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class BaseAgents(ABC):
    _module_name = "assistants"

    def _create_body(
        self,
        *,
        name: str,
        description: str | NotGiven,
        models: List[str] | NotGiven,
        tools: List[Dict[str, Any]] | NotGiven,
        tool_resources: Dict[str, Any] | NotGiven,
        requirements: List[Requirement] | NotGiven,
        budget: BudgetLevel | NotGiven,
        agent_type: AgentType | NotGiven,
        response_language: ResponseLanguage | NotGiven,
        **kwargs,
    ) -> dict:
        body = remove_not_given(
            {
                "name": name,
                "description": description,
                "models": models,
                "tools": tools,
                "tool_resources": tool_resources,
                "requirements": requirements,
                "budget": budget,
                "agent_type": agent_type,
                "response_language": response_language,
                **kwargs,
            }
        )
        # Map agent_type to assistant_type for API compatibility
        if "agent_type" in body:
            body["assistant_type"] = body.pop("agent_type")
        return body

    def _modify_body(
        self,
        *,
        name: str | NotGiven,
        description: str | NotGiven,
        models: List[str] | NotGiven,
        tools: List[Dict[str, Any]] | NotGiven,
        tool_resources: Dict[str, Any] | NotGiven,
        requirements: List[Requirement] | NotGiven,
        budget: BudgetLevel | NotGiven,
        visibility: Visibility | NotGiven,
        response_language: ResponseLanguage | NotGiven,
        **kwargs,
    ) -> dict:
        return remove_not_given(
            {
                "name": name,
                "description": description,
                "models": models,
                "tools": tools,
                "tool_resources": tool_resources,
                "requirements": requirements,
                "budget": budget,
                "visibility": visibility,
                "response_language": response_language,
                **kwargs,
            }
        )

    @abstractmethod
    def create(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        optimization: str | NotGiven = NOT_GIVEN,
        avatar: str | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Dict[str, Any]] | NotGiven = NOT_GIVEN,
        tool_resources: Dict[str, Any] | NotGiven = NOT_GIVEN,
        requirements: List[Requirement] | NotGiven = NOT_GIVEN,
        budget: BudgetLevel | NotGiven = NOT_GIVEN,
        agent_type: AgentType | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> Agent:
        pass

    @abstractmethod
    def get(self, agent_id: str) -> Agent:
        pass

    @abstractmethod
    def list(self) -> ListAgentsResponse:
        pass

    @abstractmethod
    def modify(
        self,
        agent_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        optimization: str | NotGiven = NOT_GIVEN,
        avatar: str | NotGiven = NOT_GIVEN,
        is_archived: bool | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Dict[str, Any]] | NotGiven = NOT_GIVEN,
        tool_resources: Dict[str, Any] | NotGiven = NOT_GIVEN,
        requirements: List[Requirement] | NotGiven = NOT_GIVEN,
        budget: BudgetLevel | NotGiven = NOT_GIVEN,
        visibility: Visibility | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> Agent:
        pass

    @abstractmethod
    def delete(self, agent_id: str) -> DeleteAgentResponse:
        pass
