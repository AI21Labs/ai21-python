from __future__ import annotations

from typing import Awaitable, Callable, List, Dict, Any

from ai21.clients.common.agents.agents import BaseAgents
from ai21.clients.common.agents.run import BaseAgentRun
from ai21.clients.studio.resources.maestro.maestro import AsyncMaestro
from ai21.clients.studio.resources.studio_resource import AsyncStudioResource
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
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


class AsyncAgentRuns(BaseAgentRun):
    """Async agent runs interface that delegates to maestro"""

    def __init__(self, maestro: AsyncMaestro, get_agent: Callable[[str], Awaitable[Agent]]):
        self._maestro_runs = maestro.runs
        self._get_agent = get_agent

    async def create(
        self,
        agent_id: str,
        *,
        input: str | List[MaestroMessage],
        **kwargs,
    ) -> RunResponse:
        """Create an agent run using maestro client with agent configuration"""
        agent = await self._get_agent(agent_id)
        return await self._maestro_runs.create(
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

    async def create_and_poll(
        self,
        agent_id: str,
        *,
        input: List[MaestroMessage],
        poll_interval_sec: float = DEFAULT_RUN_POLL_INTERVAL,
        poll_timeout_sec: float = DEFAULT_RUN_POLL_TIMEOUT,
        **kwargs,
    ) -> RunResponse:
        """Create and poll an agent run using maestro client"""
        agent = await self._get_agent(agent_id)

        return await self._maestro_runs.create_and_poll(
            input=input,
            **self.convert_agent_to_maestro_run_payload(agent),
            poll_interval_sec=poll_interval_sec,
            poll_timeout_sec=poll_timeout_sec,
            **kwargs,
        )


class AsyncAgents(AsyncStudioResource, BaseAgents):
    def __init__(
        self,
        client: AsyncAI21HTTPClient,
        maestro: AsyncMaestro,
    ):
        super().__init__(client)
        self.runs = AsyncAgentRuns(maestro, get_agent=self.get)

    async def create(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        optimization: str | NotGiven = NOT_GIVEN,
        avatar: str | NotGiven = NOT_GIVEN,
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
            optimization=optimization,
            avatar=avatar,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            requirements=requirements,
            budget=budget,
            response_language=response_language,
            **kwargs,
        )

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=Agent)

    async def get(self, agent_id: str) -> Agent:
        """Retrieve an agent by ID"""
        return await self._get(path=f"/{self._module_name}/{agent_id}", response_cls=Agent)

    async def list(self) -> ListAgentsResponse:
        """List all agents"""
        return await self._get(path=f"/{self._module_name}", response_cls=ListAgentsResponse)

    async def modify(
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
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            requirements=requirements,
            budget=budget,
            visibility=visibility,
            response_language=response_language,
            **kwargs,
        )
        return await self._patch(path=f"/{self._module_name}/{agent_id}", body=body, response_cls=Agent)

    async def delete(self, agent_id: str) -> DeleteAgentResponse:
        """Delete an agent"""
        return await self._delete(path=f"/{self._module_name}/{agent_id}", response_cls=DeleteAgentResponse)
