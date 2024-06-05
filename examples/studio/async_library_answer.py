import asyncio

from ai21 import AsyncAI21Client

client = AsyncAI21Client()


async def main():
    response = await client.library.answer.create(question="Can you tell me something about Holland?")
    print(response)


asyncio.run(main())
