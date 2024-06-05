import asyncio
import uuid

from ai21 import AsyncAI21Client


client = AsyncAI21Client()


async def main():
    my_datasets = await client.dataset.list()
    if len(my_datasets) > 0:
        client.custom_model.create(
            dataset_id=my_datasets[0].id,
            model_name=f"test-{(str(uuid.uuid4()))[:20]}-asaf",
            model_type="j2-mid",
        )
        my_models = client.custom_model.list()

        print(my_models)
        print(my_models[0])

        print(client.custom_model.get(my_models[0].id))


asyncio.run(main())
