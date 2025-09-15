from ai21.clients.common.agents.agents import BaseAgents
from ai21.clients.studio.resources.agents.run import AgentRun, AsyncAgentRun
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models.agents import (
    Agent,
    CreateAgentRequest,
    DeleteAgentResponse,
    ListAgentsResponse,
    ModifyAgentRequest,
)
from ai21.models._pydantic_compatibility import _to_dict


class Agents(StudioResource, BaseAgents):
    def __init__(self, client: AI21HTTPClient):
        super().__init__(client)
        self.runs = AgentRun(client)

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


class AsyncAgents(AsyncStudioResource, BaseAgents):
    def __init__(self, client: AsyncAI21HTTPClient):
        super().__init__(client)
        self.runs = AsyncAgentRun(client)

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
