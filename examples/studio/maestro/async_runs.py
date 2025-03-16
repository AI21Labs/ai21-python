import asyncio

from ai21 import AsyncAI21Client

client = AsyncAI21Client()


async def main():
    run_result = await client.beta.maestro.runs.create_and_poll(
        input="Analyze the text below and determine who's the best pokemon ever",
        context={"text": "Psyduck is the best pokemon."},
    )

    print(run_result)


if __name__ == "__main__":
    asyncio.run(main())
