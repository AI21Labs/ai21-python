import asyncio
from ai21 import AsyncAI21BedrockClient, BedrockModelID
from ai21.models.chat import ChatMessage

client = AsyncAI21BedrockClient(region="us-east-1")  # region is optional, as you can use the env variable instead

messages = [
    ChatMessage(content="You are a helpful assistant", role="system"),
    ChatMessage(content="What is the meaning of life?", role="user"),
]


async def main():
    response = await client.chat.completions.create(
        messages=messages,
        model=BedrockModelID.JAMBA_INSTRUCT_V1,
    )

    print(f"response: {response}")


asyncio.run(main())
