from ai21.clients.sagemaker.ai21_sagemaker_client import AI21SageMakerClient

client = AI21SageMakerClient(endpoint_name="j2-quantization-mid-reach-dev-cve-version-12-202313")


response = client.paraphrase.create(
    text="What's the difference between Scottish Fold and British?",
    style="formal",
)

print(response.suggestions[0].text)
