import asyncio

from ai21 import AsyncAI21VertexClient
from ai21.models.chat import ChatMessage

client = AsyncAI21VertexClient()


async def main():
    messages = ChatMessage(content="What is the meaning of life?", role="user")

    completion = await client.chat.completions.create(
        model="jamba-1.5-mini",
        messages=[messages],
    )

    print(completion)


asyncio.run(main())
