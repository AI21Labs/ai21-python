import asyncio

from ai21 import AsyncAI21SageMakerClient

client = AsyncAI21SageMakerClient(endpoint_name="sm_endpoint_name")


async def main():
    response = await client.paraphrase.create(
        text="What's the difference between Scottish Fold and British?",
        style="formal",
    )

    print(response.suggestions[0].text)


asyncio.run(main())
