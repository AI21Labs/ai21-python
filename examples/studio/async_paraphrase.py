import asyncio

from ai21 import AsyncAI21Client
from ai21.models import ParaphraseStyleType

client = AsyncAI21Client()


async def main():
    response = await client.paraphrase.create(
        text="The cat (Felis catus) is a domestic species of small carnivorous mammal",
        style=ParaphraseStyleType.GENERAL,
        start_index=0,
        end_index=20,
    )

    print(response.suggestions[0].text)
    print(response.suggestions[1].text)
    print(response.suggestions[2].text)


asyncio.run(main())
