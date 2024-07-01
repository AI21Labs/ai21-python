import asyncio

from ai21 import AsyncAI21SageMakerClient

client = AsyncAI21SageMakerClient(endpoint_name="sm_endpoint_name")


async def main():
    response = client.gec.create(text="roc and rolle")

    print(response.corrections[0].suggestion)


asyncio.run(main())
