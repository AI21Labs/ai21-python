import json

from ai21 import AI21Client


client = AI21Client(api_host="https://api-stage.ai21.com", api_key="IwOxkvOSQpbhGWVP62cWLvHCnv9poy5i")

# Create a batch

batch_requests = [
    {
        "custom_id": "request-001",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "jamba-mini",
            "messages": [{"role": "user", "content": "What is your favorite color?"}],
        },
    },
    {
        "custom_id": "request-002",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "jamba-mini",
            "messages": [{"role": "user", "content": "Tell me about your hobbies."}],
        },
    },
    {
        "custom_id": "request-003",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "jamba-mini",
            "messages": [{"role": "user", "content": "Tell me about your favorite food."}],
        },
    },
]
file_name = "batched_file.jsonl"
with open(file_name, "w") as f:
    for request in batch_requests:
        json.dump(request, f)
        f.write("\n")

# batch = client.beta.batches.create(
#     file=file_name,
#     endpoint="/v1/chat/completions",
# )

# print(batch)

# Retrieve a batch

# batch = client.batches.retrieve(batch.id)
# print(batch)

# # List batches

pages = client.beta.batches.list(limit=3)

for page in pages:
    print([batch.id for batch in page])

# # Cancel a batch

# client.batches.cancel(batch.id)


# # Get results

# results = client.batches.get_results(
#     batch_id=batch.id,
#     file_type="output",
# )
# results.write_to_file("<write path on filesystem>")
# print(results)
