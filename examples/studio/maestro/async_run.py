import asyncio

from ai21 import AsyncAI21Client

client = AsyncAI21Client()


async def main():
    try:
        run_result = await client.beta.maestro.runs.create_and_poll(
            input="Write a poem about the ocean",
            requirements=[
                {
                    "name": "length requirement",
                    "description": "The length of the poem should be less than 1000 characters",
                },
                {
                    "name": "rhyme requirement",
                    "description": "The poem should rhyme",
                },
            ],
            include=["requirements_result"],
        )

        print(run_result)
    except TimeoutError:
        print("The run timed out")


if __name__ == "__main__":
    asyncio.run(main())
