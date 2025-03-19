import asyncio

from ai21 import AsyncAI21Client


async def main():
    client = AsyncAI21Client()

    # Create a batch
    batch = await client.batches.create(
        file="<path to batched file>",
        endpoint="/v1/chat/completions",
    )

    print(batch)

    # Retrieve a batch
    batch = await client.batches.retrieve(batch.id)
    print(batch)

    # List batches
    pages = client.batches.list(limit=3)

    async for page in pages:
        print([batch.id for batch in page])

    # Cancel a batch
    await client.batches.cancel(batch.id)

    # Get results
    results = await client.batches.get_results(
        batch_id=batch.id,
        file_type="output",
    )
    results.write_to_file("<write path on filesystem>")
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
