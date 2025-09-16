from typing import List, Dict, Any

from ai21.clients.common.agents.agents import BaseAgents
from ai21.clients.studio.resources.agents.utils import AgentToMaestroRunConverter
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models.agents import (
    Agent,
    CreateAgentRequest,
    DeleteAgentResponse,
    ListAgentsResponse,
    ModifyAgentRequest,
)
from ai21.models.maestro.run import RunResponse
from ai21.models._pydantic_compatibility import _to_dict
from ai21.types import NOT_GIVEN, NotGiven


class AgentRuns:
    """Agent runs interface that delegates to maestro"""

    def __init__(self, agents_client, maestro_runs):
        self._agents_client = agents_client
        self._maestro_runs = maestro_runs

    def create(
        self,
        agent_id: str,
        *,
        input: List[Dict[str, str]],
        verbose: bool = False,
        output_type: Dict[str, Any] | NotGiven = NOT_GIVEN,
        include: List[str] | NotGiven = NOT_GIVEN,
        structured_rag_enabled: bool = False,
        dynamic_planning_enabled: bool = False,
        response_language: str = "english",
        **kwargs,
    ) -> RunResponse:
        """Create an agent run using maestro client with agent configuration"""
        agent = self._agents_client.get(agent_id)

        # Use Pydantic converter to handle parameter conversion
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

        return self._maestro_runs.create(**converter.to_maestro_create_params())

    # Delegate directly to maestro methods
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
        verbose: bool = False,
        output_type: Dict[str, Any] | NotGiven = NOT_GIVEN,
        include: List[str] | NotGiven = NOT_GIVEN,
        structured_rag_enabled: bool = False,
        dynamic_planning_enabled: bool = False,
        response_language: str = "english",
        poll_interval_sec: float = 2.0,
        poll_timeout_sec: float = 300.0,
        **kwargs,
    ) -> RunResponse:
        """Create and poll an agent run using maestro client"""
        agent = self._agents_client.get(agent_id)

        # Use Pydantic converter to handle parameter conversion
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

        return self._maestro_runs.create_and_poll(**maestro_params)


class Agents(StudioResource, BaseAgents):
    def __init__(self, client: AI21HTTPClient, maestro_runs):
        super().__init__(client)
        self.runs = AgentRuns(self, maestro_runs)

    def create(self, *, request: CreateAgentRequest) -> Agent:
        """Create a new agent"""
        # Convert agent request to assistant request format if needed
        body = _to_dict(request, exclude_none=True)
        # Map agent_type to assistant_type for API compatibility
        if "agent_type" in body:
            body["assistant_type"] = body.pop("agent_type")

        result = self._post(path=f"/{self._module_name}", body=body, response_cls=Agent)
        assert result is not None  # response_cls is provided, so result should never be None
        return result

    def get(self, agent_id: str) -> Agent:
        """Retrieve an agent by ID"""
        result = self._get(path=f"/{self._module_name}/{agent_id}", response_cls=Agent)
        assert result is not None  # response_cls is provided, so result should never be None
        return result

    def list(self) -> ListAgentsResponse:
        """List all agents"""
        result = self._get(path=f"/{self._module_name}", response_cls=ListAgentsResponse)
        assert result is not None  # response_cls is provided, so result should never be None
        return result

    def modify(self, agent_id: str, *, request: ModifyAgentRequest) -> Agent:
        """Modify an existing agent"""
        body = _to_dict(request, exclude_none=True)
        result = self._patch(path=f"/{self._module_name}/{agent_id}", body=body, response_cls=Agent)
        assert result is not None  # response_cls is provided, so result should never be None
        return result

    def delete(self, agent_id: str) -> DeleteAgentResponse:
        """Delete an agent"""
        result = self._delete(path=f"/{self._module_name}/{agent_id}", response_cls=DeleteAgentResponse)
        assert result is not None  # response_cls is provided, so result should never be None
        return result
