import asyncio

from ai21 import AsyncAI21Client
from ai21.models.chat import ChatMessage

client = AsyncAI21Client()


async def main():
    run_result = await client.maestro.runs.create_and_poll(
        messages=[ChatMessage(role="user", content="Analyze the text below and determine who's the best pokemon ever")],
        context={"text": "Psyduck is the best pokemon."},
    )

    print(run_result)


if __name__ == "__main__":
    asyncio.run(main())
