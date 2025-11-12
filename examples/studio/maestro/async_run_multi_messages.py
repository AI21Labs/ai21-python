import asyncio

from ai21 import AsyncAI21Client

client = AsyncAI21Client()


async def main():
    try:
        run_result = await client.beta.maestro.runs.create_and_poll(
            input=[
                {
                    "role": "user",
                    "content": "Write me a memo to my boss suggesting we should pivot to selling parrots. "
                    "We now have a window cleaning business for high rises",
                },
                {
                    "role": "assistant",
                    "content": "**Subject: Proposal to Pivot Business Focus**\n"
                    "**Section 1: Current Market Challenges**\n"
                    "High-rise window cleaning faces increasing competition.\n"
                    "Profit margins are shrinking due to rising operational costs.\n"
                    "Weather conditions often disrupt our service schedule.\n"
                    "**Section 2: New Opportunity in Parrot Sales**\n"
                    "Parrot sales are booming with pet ownership on the rise.\n"
                    "Parrots require minimal space and resources compared to current operations.\n"
                    "Our existing logistics can support this new venture.\n"
                    "**Section 3: Strategic Advantages**\n"
                    "Parrots offer higher profit margins than window cleaning.\n"
                    "Selling parrots expands our customer base.\n"
                    "This pivot leverages our customer service expertise",
                },
                {"role": "user", "content": "great, now beef up each section with a few more sentences"},
            ]
        )

        print(run_result)
    except TimeoutError:
        print("The run timed out")


if __name__ == "__main__":
    asyncio.run(main())
