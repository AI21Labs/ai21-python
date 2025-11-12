from ai21 import AI21Client
from ai21.models.agents import BudgetLevel, AgentType

client = AI21Client()


def main():
    """Example demonstrating CRUD operations for AI21 Agents"""

    # Create an agent
    print("Creating an agent...")
    agent = client.beta.agents.create(
        name="My Assistant",
        description="A helpful AI assistant that can answer questions",
        budget=BudgetLevel.MEDIUM,
    )

    print(f"Created agent: {agent.name} (ID: {agent.id})")
    print(f"Budget: {agent.budget}")

    agent_id = agent.id

    try:
        # Get the agent
        print(f"\nRetrieving agent {agent_id}...")
        retrieved_agent = client.beta.agents.get(agent_id)
        print(f"Retrieved agent: {retrieved_agent.name}")

        # List all agents
        print("\nListing all agents...")
        agents_list = client.beta.agents.list()
        print(f"Found {len(agents_list.results)} agents")

        # Modify the agent
        print(f"\nModifying agent {agent_id}...")
        modified_agent = client.beta.agents.modify(
            agent_id,
            name="Updated Assistant",
            description="An updated AI assistant with enhanced capabilities",
        )
        print(f"Modified agent name: {modified_agent.name}")
        print(f"Modified agent description: {modified_agent.description}")

    finally:
        # Delete the agent (cleanup)
        print(f"\nDeleting agent {agent_id}...")
        delete_response = client.beta.agents.delete(agent_id)
        print(f"Agent deleted: {delete_response.deleted}")


if __name__ == "__main__":
    main()
