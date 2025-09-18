from __future__ import annotations

from typing import Callable, List, Dict, Any

from ai21.clients.common.agents.agents import BaseAgents
from ai21.clients.common.agents.run import BaseAgentRun
from ai21.clients.studio.resources.maestro.maestro import Maestro
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models.agents import (
    Agent,
    BudgetLevel,
    DeleteAgentResponse,
    ListAgentsResponse,
    AgentRequirement,
    Visibility,
)
from ai21.models.agents.agent import ResponseLanguage
from ai21.models.maestro.run import DEFAULT_RUN_POLL_INTERVAL, DEFAULT_RUN_POLL_TIMEOUT, MaestroMessage, RunResponse
from ai21.types import NOT_GIVEN, NotGiven


class AgentRuns(BaseAgentRun):
    """Agent runs interface that delegates to maestro"""

    def __init__(self, maestro: Maestro, get_agent: Callable[[str], Agent]):
        self._get_agent = get_agent
        self._maestro_runs = maestro.runs

    def create(
        self,
        agent_id: str,
        *,
        input: str | List[MaestroMessage],
        **kwargs,
    ) -> RunResponse:
        """Create an agent run using maestro client with agent configuration"""
        agent = self._get_agent(agent_id)
        return self._maestro_runs.create(
            input=input,
            **self.convert_agent_to_maestro_run_payload(agent),
            **kwargs,
        )

    @property
    def retrieve(self):
        return self._maestro_runs.retrieve

    @property
    def poll_for_status(self):
        return self._maestro_runs.poll_for_status

    def create_and_poll(
        self,
        agent_id: str,
        *,
        input: str | List[MaestroMessage],
        poll_interval_sec: float = DEFAULT_RUN_POLL_INTERVAL,
        poll_timeout_sec: float = DEFAULT_RUN_POLL_TIMEOUT,
        **kwargs,
    ) -> RunResponse:
        """Create and poll an agent run using maestro client"""
        agent = self._get_agent(agent_id)

        return self._maestro_runs.create_and_poll(
            input=input,
            **self.convert_agent_to_maestro_run_payload(agent),
            poll_interval_sec=poll_interval_sec,
            poll_timeout_sec=poll_timeout_sec,
            **kwargs,
        )


class Agents(StudioResource, BaseAgents):
    def __init__(self, client: AI21HTTPClient, maestro: Maestro):
        super().__init__(client)
        self.runs = AgentRuns(maestro, get_agent=self.get)

    def create(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Dict[str, Any]] | NotGiven = NOT_GIVEN,
        tool_resources: Dict[str, Any] | NotGiven = NOT_GIVEN,
        requirements: List[AgentRequirement] | NotGiven = NOT_GIVEN,
        budget: BudgetLevel | NotGiven = NOT_GIVEN,
        response_language: ResponseLanguage | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> Agent:
        """Create a new agent"""
        body = self._create_body(
            name=name,
            description=description,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            requirements=requirements,
            budget=budget,
            response_language=response_language,
            **kwargs,
        )

        return self._post(path=f"/{self._module_name}", body=body, response_cls=Agent)

    def get(self, agent_id: str) -> Agent:
        """Retrieve an agent by ID"""
        return self._get(path=f"/{self._module_name}/{agent_id}", response_cls=Agent)

    def list(self) -> ListAgentsResponse:
        """List all agents"""
        return self._get(path=f"/{self._module_name}", response_cls=ListAgentsResponse)

    def modify(
        self,
        agent_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Dict[str, Any]] | NotGiven = NOT_GIVEN,
        tool_resources: Dict[str, Any] | NotGiven = NOT_GIVEN,
        requirements: List[AgentRequirement] | NotGiven = NOT_GIVEN,
        budget: BudgetLevel | NotGiven = NOT_GIVEN,
        visibility: Visibility | NotGiven = NOT_GIVEN,
        response_language: ResponseLanguage | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> Agent:
        """Modify an existing agent"""
        body = self._modify_body(
            name=name,
            description=description,
            response_language=response_language,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            requirements=requirements,
            budget=budget,
            visibility=visibility,
            **kwargs,
        )
        return self._patch(path=f"/{self._module_name}/{agent_id}", body=body, response_cls=Agent)

    def delete(self, agent_id: str) -> DeleteAgentResponse:
        """Delete an agent"""
        return self._delete(path=f"/{self._module_name}/{agent_id}", response_cls=DeleteAgentResponse)
