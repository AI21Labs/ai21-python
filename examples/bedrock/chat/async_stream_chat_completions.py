import asyncio
from ai21 import AsyncAI21BedrockClient, BedrockModelID
from ai21.models.chat import ChatMessage

client = AsyncAI21BedrockClient(region="us-east-1")  # region is optional, as you can use the env variable instead

system = "You're a support engineer in a SaaS company"
messages = [
    ChatMessage(content=system, role="system"),
    ChatMessage(content="Hello, I need help with a signup process.", role="user"),
    ChatMessage(content="Hi Alice, I can help you with that. What seems to be the problem?", role="assistant"),
    ChatMessage(content="I am having trouble signing up for your product with my Google account.", role="user"),
]


async def main():
    response = await client.chat.completions.create(
        messages=messages,
        model=BedrockModelID.JAMBA_1_5_MINI,
        max_tokens=100,
        stream=True,
    )

    async for chunk in response:
        print(chunk.choices[0].delta.content, end="")


asyncio.run(main())
