import asyncio

from ai21 import AsyncAI21Client

client = AsyncAI21Client()


async def main():
    response = await client.gec.create(text="jazzz is a great stile of music")

    print("---------------------")
    print(response.corrections[0].suggestion)
    print(response.corrections[0].start_index)
    print(response.corrections[0].end_index)
    print(response.corrections[0].original_text)
    print(response.corrections[0].correction_type)


asyncio.run(main())
