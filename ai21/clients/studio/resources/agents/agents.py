from typing import List, Dict, Any

from pydantic import Field, field_validator

from ai21.clients.common.agents.agents import BaseAgents
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.agents import (
    Agent,
    CreateAgentRequest,
    DeleteAgentResponse,
    ListAgentsResponse,
    ModifyAgentRequest,
)
from ai21.models.maestro.run import RunResponse, MaestroMessage, Budget, OutputOptions, Requirement, ToolDefinition, ToolResources
from ai21.models._pydantic_compatibility import _to_dict
from ai21.types import NOT_GIVEN, NotGiven


class Agents(StudioResource, BaseAgents):
    def __init__(self, client: AI21HTTPClient, maestro_runs):
        super().__init__(client)
        self.runs = AgentRunWrapper(self, maestro_runs)

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


class AgentToMaestroRunConverter(AI21BaseModel):
    """Pydantic model that converts agent run parameters to maestro run parameters"""
    
    # Agent inputs
    agent_id: str
    input: List[Dict[str, str]]
    verbose: bool = False
    output_type: Dict[str, Any] | NotGiven = NOT_GIVEN
    include: List[str] | NotGiven = NOT_GIVEN
    structured_rag_enabled: bool = False
    dynamic_planning_enabled: bool = False
    response_language: str = "english"
    
    # Agent configuration (will be populated from agent fetch)
    agent_models: List[str] | NotGiven = NOT_GIVEN
    agent_tools: List[Dict[str, Any]] | NotGiven = NOT_GIVEN
    agent_tool_resources: Dict[str, Any] | NotGiven = NOT_GIVEN
    agent_requirements: List[Dict[str, Any]] | NotGiven = NOT_GIVEN
    agent_budget: str | NotGiven = NOT_GIVEN
    
    # Computed maestro parameters
    maestro_input: List[MaestroMessage] = Field(default_factory=list)
    maestro_models: List[str] | NotGiven = NOT_GIVEN
    maestro_tools: List[ToolDefinition] | NotGiven = NOT_GIVEN
    maestro_tool_resources: ToolResources | NotGiven = NOT_GIVEN
    maestro_requirements: List[Requirement] | NotGiven = NOT_GIVEN
    maestro_budget: Budget | NotGiven = NOT_GIVEN
    maestro_include: List[OutputOptions] | NotGiven = NOT_GIVEN
    
    @field_validator('maestro_input', mode='before')
    @classmethod
    def convert_input_to_maestro_messages(cls, v, info):
        if 'input' in info.data:
            return [MaestroMessage(role=msg["role"], content=msg["content"]) 
                   for msg in info.data['input']]
        return v
    
    def model_post_init(self, __context) -> None:
        """Convert agent parameters to maestro parameters after initialization"""
        # Convert input messages
        self.maestro_input = [MaestroMessage(role=msg["role"], content=msg["content"]) 
                             for msg in self.input]
        
        # Map agent configuration to maestro parameters
        self.maestro_models = self.agent_models
        self.maestro_tools = self.agent_tools
        self.maestro_tool_resources = self.agent_tool_resources
        self.maestro_requirements = self.agent_requirements
        self.maestro_budget = self.agent_budget
        self.maestro_include = self.include if self.include is not NOT_GIVEN else NOT_GIVEN
    
    @classmethod
    def from_agent_and_params(
        cls,
        agent: Agent,
        agent_id: str,
        input: List[Dict[str, str]],
        verbose: bool = False,
        output_type: Dict[str, Any] | NotGiven = NOT_GIVEN,
        include: List[str] | NotGiven = NOT_GIVEN,
        structured_rag_enabled: bool = False,
        dynamic_planning_enabled: bool = False,
        response_language: str = "english",
        **kwargs
    ) -> 'AgentToMaestroRunConverter':
        """Create converter from agent configuration and run parameters"""
        agent_requirements = NOT_GIVEN
        if agent.requirements:
            agent_requirements = [req.model_dump() for req in agent.requirements]
        
        return cls(
            agent_id=agent_id,
            input=input,
            verbose=verbose,
            output_type=output_type,
            include=include,
            structured_rag_enabled=structured_rag_enabled,
            dynamic_planning_enabled=dynamic_planning_enabled,
            response_language=response_language,
            agent_models=agent.models or NOT_GIVEN,
            agent_tools=agent.tools or NOT_GIVEN,
            agent_tool_resources=agent.tool_resources or NOT_GIVEN,
            agent_requirements=agent_requirements,
            agent_budget=agent.budget.value if agent.budget else NOT_GIVEN,
            **kwargs
        )
    
    def to_maestro_create_params(self) -> dict:
        """Convert to parameters for maestro.runs.create()"""
        params = {
            "input": self.maestro_input,
            "models": self.maestro_models,
            "tools": self.maestro_tools,
            "tool_resources": self.maestro_tool_resources,
            "requirements": self.maestro_requirements,
            "budget": self.maestro_budget,
            "include": self.maestro_include,
            "response_language": self.response_language,
        }
        # Remove NOT_GIVEN values
        return {k: v for k, v in params.items() if v is not NOT_GIVEN}


class AsyncAgents(AsyncStudioResource, BaseAgents):
    def __init__(self, client: AsyncAI21HTTPClient, maestro_runs):
        super().__init__(client)
        self.runs = AsyncAgentRunWrapper(self, maestro_runs)

    async def create(self, *, request: CreateAgentRequest) -> Agent:
        """Create a new agent"""
        body = _to_dict(request, exclude_none=True)
        if "agent_type" in body:
            body["assistant_type"] = body.pop("agent_type")

        result = await self._post(path=f"/{self._module_name}", body=body, response_cls=Agent)
        assert result is not None  # response_cls is provided, so result should never be None
        return result

    async def get(self, agent_id: str) -> Agent:
        """Retrieve an agent by ID"""
        result = await self._get(path=f"/{self._module_name}/{agent_id}", response_cls=Agent)
        assert result is not None  # response_cls is provided, so result should never be None
        return result

    async def list(self) -> ListAgentsResponse:
        """List all agents"""
        result = await self._get(path=f"/{self._module_name}", response_cls=ListAgentsResponse)
        assert result is not None  # response_cls is provided, so result should never be None
        return result

    async def modify(self, agent_id: str, *, request: ModifyAgentRequest) -> Agent:
        """Modify an existing agent"""
        body = _to_dict(request, exclude_none=True)
        result = await self._patch(path=f"/{self._module_name}/{agent_id}", body=body, response_cls=Agent)
        assert result is not None  # response_cls is provided, so result should never be None
        return result

    async def delete(self, agent_id: str) -> DeleteAgentResponse:
        """Delete an agent"""
        result = await self._delete(path=f"/{self._module_name}/{agent_id}", response_cls=DeleteAgentResponse)
        assert result is not None  # response_cls is provided, so result should never be None
        return result


class AgentRunWrapper:
    """Wrapper that delegates agent runs to maestro client with agent configuration"""
    
    def __init__(self, agents_client: Agents, maestro_runs):
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
            **kwargs
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
            **kwargs
        )
        
        maestro_params = converter.to_maestro_create_params()
        maestro_params.update({
            "poll_interval_sec": poll_interval_sec,
            "poll_timeout_sec": poll_timeout_sec
        })
        
        return self._maestro_runs.create_and_poll(**maestro_params)


class AsyncAgentRunWrapper:
    """Async wrapper that delegates agent runs to maestro client with agent configuration"""
    
    def __init__(self, agents_client: AsyncAgents, maestro_runs):
        self._agents_client = agents_client
        self._maestro_runs = maestro_runs
    
    async def create(
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
        agent = await self._agents_client.get(agent_id)
        
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
            **kwargs
        )
        
        return await self._maestro_runs.create(**converter.to_maestro_create_params())
    
    # Delegate directly to maestro methods
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
        agent = await self._agents_client.get(agent_id)
        
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
            **kwargs
        )
        
        maestro_params = converter.to_maestro_create_params()
        maestro_params.update({
            "poll_interval_sec": poll_interval_sec,
            "poll_timeout_sec": poll_timeout_sec
        })
        
        return await self._maestro_runs.create_and_poll(**maestro_params)
