from ai21.clients.studio.ai21_client import AI21Client


client = AI21Client(
    api_key="9d2cf466-dd17-466e-a44f-86264eb2aec8",
    api_host="https://api.ai21-stg.com/studio/v1",
)

# print(len(client.beta.agents.list().results))

# print(client.beta.agents.get("b6c2c5b9-45ce-458e-bb42-afc8f3994aea"))

# client.beta.agents.delete("b6c2c5b9-45ce-458e-bb42-afc8f3994aea")

# print(len(client.beta.agents.list().results))

# client.beta.agents.modify(
#     agent_id="b2dc51a6-cecc-4300-b875-ee9cbb9a81dd", name="Test Agent", description="Test Agent Description"
# )

# print(client.beta.agents.get("b2dc51a6-cecc-4300-b875-ee9cbb9a81dd"))

# client.beta.agents.create(name="Test Agent2", description="Test Agent Description")

run_id = client.beta.agents.runs.create_and_poll(
    agent_id="4bf5bcbb-6454-4f87-b2b0-092af0f8af8b",
    input=[{"role": "user", "content": "What is the capital of France?"}],
)

print(run_id)
