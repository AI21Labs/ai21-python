import asyncio

from ai21 import AsyncAI21Client

file_path = "<file_path>"

client = AsyncAI21Client()


async def main():
    await client.dataset.create(file_path=file_path, dataset_name="my_new_ds_name")
    result = await client.dataset.list()
    print(result)
    first_ds_id = result[0].id
    result = await client.dataset.get(first_ds_id)
    print(result)


asyncio.run(main())
