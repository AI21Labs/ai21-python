import asyncio
from ai21 import AsyncAI21Client
from ai21.models.agents import BudgetLevel, AgentType

client = AsyncAI21Client()


async def main():
    """Example demonstrating async Agent operations with enhanced options"""

    # Create an agent
    print("Creating an agent...")
    agent = await client.beta.agents.create(
        name="Research Assistant",
        description="An AI assistant that can help with research and analysis",
        budget=BudgetLevel.MEDIUM,
    )

    print(f"Created agent: {agent.name} (ID: {agent.id})")
    agent_id = agent.id

    try:
        # Run the agent with enhanced options
        print("\nRunning agent with research question...")
        input_messages = [{"role": "user", "content": "Explain the key benefits of renewable energy"}]

        run_response = await client.beta.agents.runs.create_and_poll(
            agent_id=agent_id,
            input=input_messages,
            verbose=True,
            include=["data_sources", "requirements_result"],
            response_language="english",
            poll_timeout_sec=180,  # 3 minutes timeout
        )

        print(f"Run ID: {run_response.id}")
        print(f"Run status: {run_response.status}")

        if run_response.status == "completed":
            print("Run completed successfully!")
            if run_response.result:
                print(f"Result: {run_response.result}")

            # Show additional information if available
            if hasattr(run_response, "data_sources") and run_response.data_sources:
                print(f"Data sources used: {len(run_response.data_sources)}")

            if hasattr(run_response, "requirements_result") and run_response.requirements_result:
                print(f"Requirements result: {run_response.requirements_result}")
        else:
            print(f"Run failed with status: {run_response.status}")

        # Demonstrate multiple runs concurrently
        print("\nRunning multiple questions concurrently...")
        questions = [
            "What is photosynthesis?",
            "How do solar panels work?",
            "What are the main types of renewable energy?",
        ]

        tasks = []
        for i, question in enumerate(questions):
            input_msgs = [{"role": "user", "content": question}]
            task = client.beta.agents.runs.create_and_poll(
                agent_id=agent_id,
                input=input_msgs,
                poll_timeout_sec=120,
            )
            tasks.append(task)

        # Wait for all runs to complete
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"Question {i+1} failed: {result}")
            else:
                print(f"Question {i+1} status: {result.status}")

    except Exception as e:
        print(f"Error during agent operations: {e}")
    finally:
        # Clean up - delete the agent
        print(f"\nCleaning up - deleting agent {agent_id}...")
        await client.beta.agents.delete(agent_id)
        print("Agent deleted successfully")


if __name__ == "__main__":
    asyncio.run(main())
