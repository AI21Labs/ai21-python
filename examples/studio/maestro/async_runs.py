import asyncio

from ai21 import AsyncAI21Client

client = AsyncAI21Client()


async def main():
    run_result = await client.maestro.runs.create_and_poll(
        instruction="Who was the Maestro in the movie 'Maestro'?",
        tools=[{"type": "web_search"}],
        tool_resources={"web_search": {"urls": ["google.com"]}},
    )

    print(run_result)


if __name__ == "__main__":
    asyncio.run(main())
