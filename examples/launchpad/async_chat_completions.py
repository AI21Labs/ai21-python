import asyncio

from ai21 import AsyncAI21LaunchpadClient
from ai21.models.chat import ChatMessage


client = AsyncAI21LaunchpadClient(endpoint_id="<your_endpoint_id>")


async def main():
    messages = ChatMessage(content="What is the meaning of life?", role="user")

    completion = await client.chat.completions.create(
        model="jamba-1.6-large",
        messages=[messages],
    )

    print(completion)


asyncio.run(main())
