import httpx
import pytest
from pytest_mock import MockerFixture
from unittest.mock import patch
from uuid import uuid4

from ai21.clients.studio.resources.agents.run import AgentRun, AsyncAgentRun
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models.agents import RunResponse


@pytest.fixture
def mock_ai21_studio_client(mocker: MockerFixture) -> AI21HTTPClient:
    return mocker.MagicMock(spec=AI21HTTPClient)


@pytest.fixture
def mock_async_ai21_studio_client(mocker: MockerFixture) -> AsyncAI21HTTPClient:
    return mocker.MagicMock(spec=AsyncAI21HTTPClient)


def get_dummy_run_response(status="completed"):
    run_id = str(uuid4())
    response = {
        "id": run_id,
        "status": status,
        "data_sources": {"file_search": []},
        "requirements_result": None,
    }

    # Only include result field for completed runs
    if status == "completed":
        response["result"] = "This is the agent's response"

    return response


class TestAgentRun:
    def test_create_run(self, mock_ai21_studio_client):
        # Arrange
        agent_id = str(uuid4())
        run_data = get_dummy_run_response()
        input_messages = [{"role": "user", "content": "Hello, agent!"}]

        mock_response = httpx.Response(status_code=200, json=run_data)
        mock_ai21_studio_client.execute_http_request.return_value = mock_response

        agent_run = AgentRun(mock_ai21_studio_client)

        # Act
        result = agent_run.create(agent_id, input=input_messages)

        # Assert
        assert isinstance(result, RunResponse)
        assert result.status == "completed"
        assert result.result == "This is the agent's response"

        # Verify the API call
        mock_ai21_studio_client.execute_http_request.assert_called_once()
        args, kwargs = mock_ai21_studio_client.execute_http_request.call_args
        assert kwargs["method"] == "POST"
        assert kwargs["path"] == f"/assistants/{agent_id}/run"

        body = kwargs["body"]
        assert body["input"] == input_messages
        assert body["verbose"] is False
        assert body["response_language"] == "unset"

    def test_create_run_with_all_options(self, mock_ai21_studio_client):
        # Arrange
        agent_id = str(uuid4())
        run_data = get_dummy_run_response()
        input_messages = [{"role": "user", "content": "Hello, agent!"}]

        mock_response = httpx.Response(status_code=200, json=run_data)
        mock_ai21_studio_client.execute_http_request.return_value = mock_response

        agent_run = AgentRun(mock_ai21_studio_client)

        # Act
        result = agent_run.create(
            agent_id,
            input=input_messages,
            verbose=True,
            include=["data_sources", "requirements_result"],
            structured_rag_enabled=True,
            dynamic_planning_enabled=True,
            response_language="english",
        )

        # Assert
        assert isinstance(result, RunResponse)

        # Verify the API call body
        args, kwargs = mock_ai21_studio_client.execute_http_request.call_args
        body = kwargs["body"]
        assert body["verbose"] is True
        assert body["include"] == ["data_sources", "requirements_result"]
        assert body["structured_rag_enabled"] is True
        assert body["dynamic_planning_enabled"] is True
        assert body["response_language"] == "english"

    def test_retrieve_run(self, mock_ai21_studio_client):
        # Arrange
        run_id = str(uuid4())
        run_data = get_dummy_run_response()
        run_data["id"] = run_id

        mock_response = httpx.Response(status_code=200, json=run_data)
        mock_ai21_studio_client.execute_http_request.return_value = mock_response

        agent_run = AgentRun(mock_ai21_studio_client)

        # Act
        result = agent_run.retrieve(run_id)

        # Assert
        assert isinstance(result, RunResponse)
        assert str(result.id) == run_id
        assert result.status == "completed"

        mock_ai21_studio_client.execute_http_request.assert_called_once_with(
            method="GET", path=f"/maestro/runs/{run_id}", params={}
        )

    @patch("time.time")
    @patch("time.sleep")
    def test_poll_for_status_success(self, mock_sleep, mock_time, mock_ai21_studio_client):
        # Arrange
        run_id = str(uuid4())

        # Mock time.time() to return increasing values
        mock_time.side_effect = [0, 1, 2, 3]  # Simulate time passing

        # First call returns in_progress, second returns completed
        in_progress_data = get_dummy_run_response("in_progress")
        completed_data = get_dummy_run_response("completed")

        mock_ai21_studio_client.execute_http_request.side_effect = [
            httpx.Response(status_code=200, json=in_progress_data),
            httpx.Response(status_code=200, json=completed_data),
        ]

        agent_run = AgentRun(mock_ai21_studio_client)

        # Act
        result = agent_run.poll_for_status(run_id=run_id, poll_interval_sec=1.0, poll_timeout_sec=30.0)

        # Assert
        assert result.status == "completed"
        assert mock_ai21_studio_client.execute_http_request.call_count == 2
        mock_sleep.assert_called_once_with(1.0)

    @patch("time.time")
    def test_poll_for_status_timeout(self, mock_time, mock_ai21_studio_client):
        # Arrange
        run_id = str(uuid4())

        # Mock time to simulate timeout
        mock_time.side_effect = [0, 31]  # Start at 0, then jump to 31 seconds

        in_progress_data = get_dummy_run_response("in_progress")
        mock_ai21_studio_client.execute_http_request.return_value = httpx.Response(
            status_code=200, json=in_progress_data
        )

        agent_run = AgentRun(mock_ai21_studio_client)

        # Act & Assert
        with pytest.raises(TimeoutError) as exc_info:
            agent_run.poll_for_status(run_id=run_id, poll_interval_sec=1.0, poll_timeout_sec=30.0)

        assert "Timeout of 30.0 while polling" in str(exc_info.value)

    def test_create_and_poll(self, mock_ai21_studio_client):
        # Arrange
        agent_id = str(uuid4())
        run_data = get_dummy_run_response()
        input_messages = [{"role": "user", "content": "Hello, agent!"}]

        # Mock the create call
        mock_response = httpx.Response(status_code=200, json=run_data)
        mock_ai21_studio_client.execute_http_request.return_value = mock_response

        # Mock the retrieve call (for polling)
        mock_ai21_studio_client.execute_http_request.return_value = mock_response

        agent_run = AgentRun(mock_ai21_studio_client)

        # Act
        result = agent_run.create_and_poll(agent_id, input=input_messages)

        # Assert
        assert isinstance(result, RunResponse)
        assert result.status == "completed"

        # Verify both create and retrieve were called
        assert mock_ai21_studio_client.execute_http_request.call_count == 2


class TestAsyncAgentRun:
    @pytest.mark.asyncio
    async def test_create_run(self, mock_async_ai21_studio_client):
        # Arrange
        agent_id = str(uuid4())
        run_data = get_dummy_run_response()
        input_messages = [{"role": "user", "content": "Hello, agent!"}]

        mock_response = httpx.Response(status_code=200, json=run_data)
        mock_async_ai21_studio_client.execute_http_request.return_value = mock_response

        agent_run = AsyncAgentRun(mock_async_ai21_studio_client)

        # Act
        result = await agent_run.create(agent_id, input=input_messages)

        # Assert
        assert isinstance(result, RunResponse)
        assert result.status == "completed"
        assert result.result == "This is the agent's response"

    @pytest.mark.asyncio
    async def test_retrieve_run(self, mock_async_ai21_studio_client):
        # Arrange
        run_id = str(uuid4())
        run_data = get_dummy_run_response()
        run_data["id"] = run_id

        mock_response = httpx.Response(status_code=200, json=run_data)
        mock_async_ai21_studio_client.execute_http_request.return_value = mock_response

        agent_run = AsyncAgentRun(mock_async_ai21_studio_client)

        # Act
        result = await agent_run.retrieve(run_id)

        # Assert
        assert isinstance(result, RunResponse)
        assert str(result.id) == run_id
        assert result.status == "completed"

    @pytest.mark.asyncio
    @patch("time.time")
    @patch("asyncio.sleep")
    async def test_poll_for_status_success(self, mock_sleep, mock_time, mock_async_ai21_studio_client):
        # Arrange
        run_id = str(uuid4())

        # Mock time.time() to return increasing values
        mock_time.side_effect = [0, 1, 2, 3]

        # Mock asyncio.sleep to be async
        mock_sleep.return_value = None

        # First call returns in_progress, second returns completed
        in_progress_data = get_dummy_run_response("in_progress")
        completed_data = get_dummy_run_response("completed")

        mock_async_ai21_studio_client.execute_http_request.side_effect = [
            httpx.Response(status_code=200, json=in_progress_data),
            httpx.Response(status_code=200, json=completed_data),
        ]

        agent_run = AsyncAgentRun(mock_async_ai21_studio_client)

        # Act
        result = await agent_run.poll_for_status(run_id=run_id, poll_interval_sec=1.0, poll_timeout_sec=30.0)

        # Assert
        assert result.status == "completed"
        assert mock_async_ai21_studio_client.execute_http_request.call_count == 2
        mock_sleep.assert_called_once_with(1.0)

    @pytest.mark.asyncio
    async def test_create_and_poll(self, mock_async_ai21_studio_client):
        # Arrange
        agent_id = str(uuid4())
        run_data = get_dummy_run_response()
        input_messages = [{"role": "user", "content": "Hello, agent!"}]

        # Mock the create call
        mock_response = httpx.Response(status_code=200, json=run_data)
        mock_async_ai21_studio_client.execute_http_request.return_value = mock_response

        # Mock the retrieve call (for polling)
        mock_async_ai21_studio_client.execute_http_request.return_value = mock_response

        agent_run = AsyncAgentRun(mock_async_ai21_studio_client)

        # Act
        result = await agent_run.create_and_poll(agent_id, input=input_messages)

        # Assert
        assert isinstance(result, RunResponse)
        assert result.status == "completed"

        # Verify both create and retrieve were called
        assert mock_async_ai21_studio_client.execute_http_request.call_count == 2
