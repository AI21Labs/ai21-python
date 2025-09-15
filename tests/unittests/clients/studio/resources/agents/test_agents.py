import httpx
import pytest
from pytest_mock import MockerFixture
from uuid import uuid4

from ai21.clients.studio.resources.agents.agents import Agents, AsyncAgents
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models.agents import (
    Agent,
    AgentType,
    BudgetLevel,
    CreateAgentRequest,
    DeleteAgentResponse,
    ListAgentsResponse,
    ModifyAgentRequest,
    Requirement,
    Visibility,
)
from ai21.models._pydantic_compatibility import _from_dict, _to_dict


@pytest.fixture
def mock_ai21_studio_client(mocker: MockerFixture) -> AI21HTTPClient:
    return mocker.MagicMock(spec=AI21HTTPClient)


@pytest.fixture
def mock_async_ai21_studio_client(mocker: MockerFixture) -> AsyncAI21HTTPClient:
    return mocker.MagicMock(spec=AsyncAI21HTTPClient)


def get_dummy_agent_data():
    agent_id = str(uuid4())
    return {
        "id": agent_id,
        "name": "Test Agent",
        "description": "A test agent",
        "organization_id": "org-123",
        "user_id": "user-456",
        "budget": "medium",
        "visibility": "public",
        "agent_type": "default",
        "created_at": "2023-01-01T00:00:00Z",
        "updated_at": "2023-01-01T00:00:00Z",
        "object": "agent",
        "is_archived": False,
    }


def get_dummy_create_request():
    return CreateAgentRequest(
        name="Test Agent",
        description="A test agent",
        budget=BudgetLevel.MEDIUM,
        agent_type=AgentType.DEFAULT,
    )


class TestAgents:
    def test_create_agent(self, mock_ai21_studio_client):
        # Arrange
        agent_data = get_dummy_agent_data()
        request = get_dummy_create_request()
        
        mock_response = httpx.Response(status_code=200, json=agent_data)
        mock_ai21_studio_client.execute_http_request.return_value = mock_response
        
        agents = Agents(mock_ai21_studio_client)
        
        # Act
        result = agents.create(request=request)
        
        # Assert
        assert isinstance(result, Agent)
        assert result.name == "Test Agent"
        assert result.budget == BudgetLevel.MEDIUM
        
        # Verify the API call
        mock_ai21_studio_client.execute_http_request.assert_called_once()
        args, kwargs = mock_ai21_studio_client.execute_http_request.call_args
        assert kwargs["method"] == "POST"
        assert kwargs["path"] == "/assistants"
        
        # Check that agent_type was mapped to assistant_type
        body = kwargs["body"]
        assert "assistant_type" in body
        assert body["assistant_type"] == "default"
        assert "agent_type" not in body

    def test_get_agent(self, mock_ai21_studio_client):
        # Arrange
        agent_data = get_dummy_agent_data()
        agent_id = agent_data["id"]
        
        mock_response = httpx.Response(status_code=200, json=agent_data)
        mock_ai21_studio_client.execute_http_request.return_value = mock_response
        
        agents = Agents(mock_ai21_studio_client)
        
        # Act
        result = agents.get(agent_id)
        
        # Assert
        assert isinstance(result, Agent)
        assert result.id == agent_id
        assert result.name == "Test Agent"
        
        mock_ai21_studio_client.execute_http_request.assert_called_once_with(
            method="GET",
            path=f"/assistants/{agent_id}",
            params={}
        )

    def test_list_agents(self, mock_ai21_studio_client):
        # Arrange
        agent_data = get_dummy_agent_data()
        list_response = {"results": [agent_data]}
        
        mock_response = httpx.Response(status_code=200, json=list_response)
        mock_ai21_studio_client.execute_http_request.return_value = mock_response
        
        agents = Agents(mock_ai21_studio_client)
        
        # Act
        result = agents.list()
        
        # Assert
        assert isinstance(result, ListAgentsResponse)
        assert len(result.results) == 1
        assert result.results[0].name == "Test Agent"
        
        mock_ai21_studio_client.execute_http_request.assert_called_once_with(
            method="GET",
            path="/assistants",
            params={}
        )

    def test_modify_agent(self, mock_ai21_studio_client):
        # Arrange
        agent_data = get_dummy_agent_data()
        agent_id = agent_data["id"]
        agent_data["name"] = "Modified Agent"
        
        modify_request = ModifyAgentRequest(name="Modified Agent")
        
        mock_response = httpx.Response(status_code=200, json=agent_data)
        mock_ai21_studio_client.execute_http_request.return_value = mock_response
        
        agents = Agents(mock_ai21_studio_client)
        
        # Act
        result = agents.modify(agent_id, request=modify_request)
        
        # Assert
        assert isinstance(result, Agent)
        assert result.name == "Modified Agent"
        
        mock_ai21_studio_client.execute_http_request.assert_called_once_with(
            method="PATCH",
            path=f"/assistants/{agent_id}",
            body={"name": "Modified Agent"}
        )

    def test_delete_agent(self, mock_ai21_studio_client):
        # Arrange
        agent_id = str(uuid4())
        delete_response = {"object": "agent", "deleted": True, "id": agent_id}
        
        mock_response = httpx.Response(status_code=200, json=delete_response)
        mock_ai21_studio_client.execute_http_request.return_value = mock_response
        
        agents = Agents(mock_ai21_studio_client)
        
        # Act
        result = agents.delete(agent_id)
        
        # Assert
        assert isinstance(result, DeleteAgentResponse)
        assert result.deleted is True
        assert result.id == agent_id
        
        mock_ai21_studio_client.execute_http_request.assert_called_once_with(
            method="DELETE",
            path=f"/assistants/{agent_id}"
        )


class TestAsyncAgents:
    @pytest.mark.asyncio
    async def test_create_agent(self, mock_async_ai21_studio_client):
        # Arrange
        agent_data = get_dummy_agent_data()
        request = get_dummy_create_request()
        
        mock_response = httpx.Response(status_code=200, json=agent_data)
        mock_async_ai21_studio_client.execute_http_request.return_value = mock_response
        
        agents = AsyncAgents(mock_async_ai21_studio_client)
        
        # Act
        result = await agents.create(request=request)
        
        # Assert
        assert isinstance(result, Agent)
        assert result.name == "Test Agent"
        assert result.budget == BudgetLevel.MEDIUM
        
        # Verify the API call
        mock_async_ai21_studio_client.execute_http_request.assert_called_once()
        args, kwargs = mock_async_ai21_studio_client.execute_http_request.call_args
        assert kwargs["method"] == "POST"
        assert kwargs["path"] == "/assistants"

    @pytest.mark.asyncio
    async def test_get_agent(self, mock_async_ai21_studio_client):
        # Arrange
        agent_data = get_dummy_agent_data()
        agent_id = agent_data["id"]
        
        mock_response = httpx.Response(status_code=200, json=agent_data)
        mock_async_ai21_studio_client.execute_http_request.return_value = mock_response
        
        agents = AsyncAgents(mock_async_ai21_studio_client)
        
        # Act
        result = await agents.get(agent_id)
        
        # Assert
        assert isinstance(result, Agent)
        assert result.id == agent_id
        assert result.name == "Test Agent"

    @pytest.mark.asyncio
    async def test_list_agents(self, mock_async_ai21_studio_client):
        # Arrange
        agent_data = get_dummy_agent_data()
        list_response = {"results": [agent_data]}
        
        mock_response = httpx.Response(status_code=200, json=list_response)
        mock_async_ai21_studio_client.execute_http_request.return_value = mock_response
        
        agents = AsyncAgents(mock_async_ai21_studio_client)
        
        # Act
        result = await agents.list()
        
        # Assert
        assert isinstance(result, ListAgentsResponse)
        assert len(result.results) == 1
        assert result.results[0].name == "Test Agent"

    @pytest.mark.asyncio
    async def test_modify_agent(self, mock_async_ai21_studio_client):
        # Arrange
        agent_data = get_dummy_agent_data()
        agent_id = agent_data["id"]
        agent_data["name"] = "Modified Agent"
        
        modify_request = ModifyAgentRequest(name="Modified Agent")
        
        mock_response = httpx.Response(status_code=200, json=agent_data)
        mock_async_ai21_studio_client.execute_http_request.return_value = mock_response
        
        agents = AsyncAgents(mock_async_ai21_studio_client)
        
        # Act
        result = await agents.modify(agent_id, request=modify_request)
        
        # Assert
        assert isinstance(result, Agent)
        assert result.name == "Modified Agent"

    @pytest.mark.asyncio
    async def test_delete_agent(self, mock_async_ai21_studio_client):
        # Arrange
        agent_id = str(uuid4())
        delete_response = {"object": "agent", "deleted": True, "id": agent_id}
        
        mock_response = httpx.Response(status_code=200, json=delete_response)
        mock_async_ai21_studio_client.execute_http_request.return_value = mock_response
        
        agents = AsyncAgents(mock_async_ai21_studio_client)
        
        # Act
        result = await agents.delete(agent_id)
        
        # Assert
        assert isinstance(result, DeleteAgentResponse)
        assert result.deleted is True
        assert result.id == agent_id