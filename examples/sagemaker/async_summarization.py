import asyncio

from ai21 import AsyncAI21SageMakerClient

client = AsyncAI21SageMakerClient(endpoint_name="sm_endpoint_name")


async def main():
    response = await client.summarize.create(
        source="Holland is a geographical region[2] and former province on the western coast of the Netherlands.[2]"
        " From the 10th to the 16th century, "
        "Holland proper was a unified political region within the Holy Roman Empire as a"
        " county ruled by the counts of Holland. By the 17th century, "
        "the province of Holland had risen to become a maritime and economic power,"
        " dominating the other provinces of the newly independent Dutch "
        "Republic.",
        source_type="TEXT",
    )

    print(response.summary)


asyncio.run(main())
