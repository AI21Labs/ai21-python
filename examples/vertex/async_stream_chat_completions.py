import asyncio

from ai21 import AsyncAI21VertexClient

from ai21.models.chat import ChatMessage

client = AsyncAI21VertexClient()

messages = ChatMessage(content="What is the meaning of life?", role="user")


async def main():
    completion = await client.chat.completions.create(
        model="jamba-instruct",
        messages=[messages],
        stream=True,
    )

    async for chunk in completion:
        print(chunk.choices[0].delta.content, end="")


asyncio.run(main())
