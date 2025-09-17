from typing import Awaitable, Callable, List, Dict, Any, Union

from ai21.clients.common.agents.agents import BaseAgents
from ai21.clients.common.agents.run import BaseAgentRun
from ai21.clients.studio.resources.maestro.maestro import AsyncMaestro
from ai21.clients.studio.resources.maestro.run import AsyncMaestroRun
from ai21.clients.studio.resources.studio_resource import AsyncStudioResource
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.models.agents import (
    Agent,
    AgentType,
    BudgetLevel,
    DeleteAgentResponse,
    ListAgentsResponse,
    Requirement,
    Visibility,
)
from ai21.models.maestro.run import RunResponse
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
        input: List[Dict[str, str]],
        verbose: bool = False,
        output_type: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        include: Union[List[str], NotGiven] = NOT_GIVEN,
        structured_rag_enabled: bool = False,
        dynamic_planning_enabled: bool = False,
        response_language: str = "english",
        **kwargs,
    ) -> RunResponse:
        """Create an agent run using maestro client with agent configuration"""
        agent = await self._get_agent(agent_id)

        converter = AgentToMaestroRunConverter.from_agent_and_params(
            agent=agent,
            agent_id=agent_id,
            input=input,
            verbose=verbose,
            output_type=output_type,
            include=include,
            structured_rag_enabled=structured_rag_enabled,
            dynamic_planning_enabled=dynamic_planning_enabled,
            response_language=response_language,
            **kwargs,
        )

        return await self._maestro_runs.create(**converter.to_maestro_create_params())

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
        input: List[Dict[str, str]],
        verbose: bool = False,
        output_type: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        include: Union[List[str], NotGiven] = NOT_GIVEN,
        structured_rag_enabled: bool = False,
        dynamic_planning_enabled: bool = False,
        response_language: str = "english",
        poll_interval_sec: float = 2.0,
        poll_timeout_sec: float = 300.0,
        **kwargs,
    ) -> RunResponse:
        """Create and poll an agent run using maestro client"""
        agent = await self._get_agent(agent_id)

        converter = AgentToMaestroRunConverter.from_agent_and_params(
            agent=agent,
            agent_id=agent_id,
            input=input,
            verbose=verbose,
            output_type=output_type,
            include=include,
            structured_rag_enabled=structured_rag_enabled,
            dynamic_planning_enabled=dynamic_planning_enabled,
            response_language=response_language,
            **kwargs,
        )

        maestro_params = converter.to_maestro_create_params()
        maestro_params.update({"poll_interval_sec": poll_interval_sec, "poll_timeout_sec": poll_timeout_sec})

        return await self._maestro_runs.create_and_poll(**maestro_params)


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
        requirements: List[Requirement] | NotGiven = NOT_GIVEN,
        budget: BudgetLevel | NotGiven = NOT_GIVEN,
        agent_type: AgentType | NotGiven = NOT_GIVEN,
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
            agent_type=agent_type,
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
        """Modify an existing agent"""
        body = self._modify_body(
            name=name,
            description=description,
            optimization=optimization,
            avatar=avatar,
            is_archived=is_archived,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            requirements=requirements,
            budget=budget,
            visibility=visibility,
            **kwargs,
        )
        return await self._patch(path=f"/{self._module_name}/{agent_id}", body=body, response_cls=Agent)

    async def delete(self, agent_id: str) -> DeleteAgentResponse:
        """Delete an agent"""
        return await self._delete(path=f"/{self._module_name}/{agent_id}", response_cls=DeleteAgentResponse)
