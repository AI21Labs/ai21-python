from ai21.clients.sagemaker.ai21_sagemaker_client import AI21SageMakerClient

client = AI21SageMakerClient(endpoint_name="j2-quantization-mid-reach-dev-cve-version-12-202313")
response = client.gec.create(text="roc and rolle")

print(response.corrections[0].suggestion)
