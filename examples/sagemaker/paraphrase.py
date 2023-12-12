from ai21 import AI21SageMakerClient

client = AI21SageMakerClient(endpoint_name="sm_endpoint_name")


response = client.paraphrase.create(
    text="What's the difference between Scottish Fold and British?",
    style="formal",
)

print(response.suggestions[0].text)
