from ai21 import AI21Client
from ai21.models.agents import BudgetLevel, AgentType

client = AI21Client()


def main():
    """Example demonstrating how to create and run an AI21 Agent"""

    # Create an agent
    print("Creating an agent...")
    agent = client.beta.agents.create(
        name="Math Assistant",
        description="An AI assistant specialized in solving math problems",
        budget=BudgetLevel.LOW,
    )

    print(f"Created agent: {agent.name} (ID: {agent.id})")
    agent_id = agent.id

    try:
        # Run the agent with a simple math question
        print("\nRunning agent with math question...")
        input_messages = [{"role": "user", "content": "What is 15 * 23? Please show your work."}]

        run_response = client.beta.agents.runs.create_and_poll(
            agent_id=agent_id,
            input=input_messages,
            poll_timeout_sec=120,  # 2 minutes timeout
        )

        print(f"Run ID: {run_response.id}")
        print(f"Run status: {run_response.status}")

        if run_response.status == "completed":
            print("Run completed successfully!")
            if run_response.result:
                print(f"Result: {run_response.result}")
        else:
            print(f"Run failed with status: {run_response.status}")

        # Retrieve the run to show how to get run details
        print(f"\nRetrieving run details...")
        retrieved_run = client.beta.agents.runs.retrieve(str(run_response.id))
        print(f"Retrieved run status: {retrieved_run.status}")

    except Exception as e:
        print(f"Error during agent run: {e}")
    finally:
        # Clean up - delete the agent
        print(f"\nCleaning up - deleting agent {agent_id}...")
        client.beta.agents.delete(agent_id)
        print("Agent deleted successfully")


if __name__ == "__main__":
    main()
