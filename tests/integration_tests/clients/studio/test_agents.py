import pytest

from ai21 import AsyncAI21Client
from ai21.models.agents import BudgetLevel


@pytest.mark.asyncio
async def test_agents_create_and_delete():
    """Test creating and deleting an agent"""
    client = AsyncAI21Client()

    # Create an agent
    agent = await client.beta.agents.create(
        name="Test Agent for Integration",
        description="This is a test agent created by integration tests",
        budget=BudgetLevel.LOW,
    )

    # Verify agent was created
    assert agent.id is not None
    assert agent.name == "Test Agent for Integration"
    assert agent.description == "This is a test agent created by integration tests"
    assert agent.budget == BudgetLevel.LOW
    assert agent.object == "agent"

    # Clean up - delete the agent
    delete_response = await client.beta.agents.delete(agent.id)
    assert delete_response.deleted is True
    assert delete_response.id == agent.id


@pytest.mark.asyncio
async def test_agents_crud_operations():
    """Test full CRUD operations for agents"""
    client = AsyncAI21Client()

    # Create
    agent = await client.beta.agents.create(
        name="CRUD Test Agent",
        description="Testing CRUD operations",
        budget=BudgetLevel.MEDIUM,
    )
    agent_id = agent.id

    try:
        # Read - Get specific agent
        retrieved_agent = await client.beta.agents.get(agent_id)
        assert retrieved_agent.id == agent_id
        assert retrieved_agent.name == "CRUD Test Agent"

        # Read - List agents (should include our agent)
        agents_list = await client.beta.agents.list()
        agent_ids = [a.id for a in agents_list.results]
        assert agent_id in agent_ids

        # Update
        updated_agent = await client.beta.agents.modify(
            agent_id,
            name="Modified CRUD Test Agent",
            description="Updated description for testing",
        )
        assert updated_agent.id == agent_id
        assert updated_agent.name == "Modified CRUD Test Agent"
        assert updated_agent.description == "Updated description for testing"

    finally:
        # Delete
        delete_response = await client.beta.agents.delete(agent_id)
        assert delete_response.deleted is True


@pytest.mark.asyncio
async def test_agent_run_basic():
    """Test running an agent with basic input"""
    client = AsyncAI21Client()

    # Create a test agent
    agent = await client.beta.agents.create(
        name="Test Run Agent",
        description="Agent for testing runs",
        budget=BudgetLevel.LOW,
    )
    agent_id = agent.id

    try:
        # Test agent run
        input_messages = [{"role": "user", "content": "What is 2+2?"}]

        run_response = await client.beta.agents.runs.create_and_poll(
            agent_id,
            input=input_messages,
            poll_timeout_sec=120,  # 2 minutes timeout
        )

        assert run_response.id is not None
        assert run_response.status in ["completed", "failed"]

        if run_response.status == "completed":
            assert run_response.result is not None

        # Test retrieving the run
        retrieved_run = await client.beta.agents.runs.retrieve(str(run_response.id))
        assert retrieved_run.id == run_response.id
        assert retrieved_run.status == run_response.status

    finally:
        # Clean up
        await client.beta.agents.delete(agent_id)


@pytest.mark.asyncio
async def test_agent_run_with_options():
    """Test running an agent with various options"""
    client = AsyncAI21Client()

    # Create a test agent
    agent = await client.beta.agents.create(
        name="Test Options Agent",
        description="Agent for testing run options",
        budget=BudgetLevel.MEDIUM,
    )
    agent_id = agent.id

    try:
        # Test agent run with options
        input_messages = [{"role": "user", "content": "Tell me about AI"}]

        run_response = await client.beta.agents.runs.create_and_poll(
            agent_id,
            input=input_messages,
            verbose=True,
            include=["data_sources", "requirements_result"],
            response_language="english",
            poll_timeout_sec=120,
        )

        assert run_response.id is not None
        assert run_response.status in ["completed", "failed"]

        if run_response.status == "completed":
            assert run_response.result is not None

    finally:
        # Clean up
        await client.beta.agents.delete(agent_id)


@pytest.mark.asyncio
async def test_agents_list_empty_or_populated():
    """Test listing agents when there may be none or some"""
    client = AsyncAI21Client()

    # List all agents
    agents_list = await client.beta.agents.list()

    # Should return a valid response
    assert hasattr(agents_list, "results")
    assert isinstance(agents_list.results, list)

    # Each result should be a proper Agent object
    for agent in agents_list.results:
        assert hasattr(agent, "id")
        assert hasattr(agent, "name")
        assert hasattr(agent, "created_at")
        assert hasattr(agent, "updated_at")
