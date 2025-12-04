import asyncio

from ai21 import AsyncAI21Client

client = AsyncAI21Client()


async def main():
    try:
        run_result = await client.beta.maestro.runs.create_and_poll(
            input="Tell me about AI21 Maestro",
            requirements=[
                {
                    "name": "length requirement",
                    "description": "The length of the response should be less than 2000 characters",
                },
                {
                    "name": "source requirement",
                    "description": (
                        "Should rely on information from these websites: "
                        "https://www.ai21.com/, https://www.ai21.com/maestro/, "
                        "https://docs.ai21.com/home"
                    ),
                },
            ],
            include=["requirements_result"],
        )
        print(run_result)
    except TimeoutError:
        print("The run timed out")


if __name__ == "__main__":
    asyncio.run(main())
