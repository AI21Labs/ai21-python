import asyncio

from ai21 import AsyncAI21Client
from ai21.models import EmbedType

client = AsyncAI21Client()


async def main():
    response = await client.embed.create(
        texts=["Holland is a geographical region[2] and former province on the western coast of the Netherlands."],
        type=EmbedType.SEGMENT,
    )
    print("embed: ", response.results[0].embedding)


asyncio.run(main())
