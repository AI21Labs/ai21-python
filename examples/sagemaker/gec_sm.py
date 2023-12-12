from ai21 import AI21SageMakerClient

client = AI21SageMakerClient(endpoint_name="sm_endpoint_name")
response = client.gec.create(text="roc and rolle")

print(response.corrections[0].suggestion)
