import asyncio

from ai21 import AsyncAI21Client
from ai21.models.chat import ChatMessage

system = "You're a support engineer in a SaaS company"
messages = [
    ChatMessage(content=system, role="system"),
    ChatMessage(content="Hello, I need help with a signup process.", role="user"),
    ChatMessage(content="Hi Alice, I can help you with that. What seems to be the problem?", role="assistant"),
    ChatMessage(content="I am having trouble signing up for your product with my Google account.", role="user"),
]

client = AsyncAI21Client()


async def main():
    response = await client.chat.completions.create(
        messages=messages,
        model="jamba-instruct-preview",
        max_tokens=100,
        stream=True,
    )
    async for chunk in response:
        print(chunk.choices[0].delta.content, end="")


asyncio.run(main())
