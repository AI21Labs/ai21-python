import asyncio

from ai21 import AsyncAI21Client

client = AsyncAI21Client()


async def main():
    response = await client.library.search.create(query="cat colors", max_segments=2)
    print(response)


asyncio.run(main())
