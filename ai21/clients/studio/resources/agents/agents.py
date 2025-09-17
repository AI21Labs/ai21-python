from typing import Callable, List, Dict, Any, Union

from ai21.clients.common.agents.agents import BaseAgents
from ai21.clients.common.agents.run import BaseAgentRun
from ai21.clients.studio.resources.maestro.maestro import Maestro
from ai21.clients.studio.resources.maestro.run import MaestroRun
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.http_client.http_client import AI21HTTPClient
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
from ai21.models.maestro.run import RunResponse
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
        input: List[Dict[str, str]],
        verbose: bool = False,
        output_type: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        include: Union[List[str], NotGiven] = NOT_GIVEN,
        structured_rag_enabled: bool | NotGiven = NOT_GIVEN,
        dynamic_planning_enabled: bool | NotGiven = NOT_GIVEN,
        response_language: ResponseLanguage | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> RunResponse:
        """Create an agent run using maestro client with agent configuration"""
        agent = self._get_agent(agent_id)

        converter = self._create_agent_to_maestro_converter(
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

        return self._maestro_runs.create(**converter.to_maestro_create_params())

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
        input: List[Dict[str, str]],
        verbose: Union[bool, NotGiven] = NOT_GIVEN,
        output_type: Union[Dict[str, Any], NotGiven] = NOT_GIVEN,
        include: Union[List[str], NotGiven] = NOT_GIVEN,
        structured_rag_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        dynamic_planning_enabled: Union[bool, NotGiven] = NOT_GIVEN,
        response_language: Union[ResponseLanguage, NotGiven] = NOT_GIVEN,
        poll_interval_sec: Union[float, NotGiven] = NOT_GIVEN,
        poll_timeout_sec: Union[float, NotGiven] = NOT_GIVEN,
        **kwargs,
    ) -> RunResponse:
        """Create and poll an agent run using maestro client"""
        agent = self._get_agent(agent_id)

        converter = self._create_agent_to_maestro_converter(
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

        return self._maestro_runs.create_and_poll(**maestro_params)


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
        requirements: List[Requirement] | NotGiven = NOT_GIVEN,
        budget: BudgetLevel | NotGiven = NOT_GIVEN,
        agent_type: AgentType | NotGiven = NOT_GIVEN,
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
            agent_type=agent_type,
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
        requirements: List[Requirement] | NotGiven = NOT_GIVEN,
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
