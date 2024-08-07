import asyncio
import os
import uuid

from ai21 import AsyncAI21Client
from ai21.models.chat import ChatMessage
from examples.studio import file_utils

messages = [
    ChatMessage(content="<Write a question about your file here>", role="user"),
]


async def upload_file(client: AsyncAI21Client):
    file_name = f"test-file-{uuid.uuid4()}.txt"
    file_path = os.getcwd()

    path = os.path.join(file_path, file_name)
    file_utils.create_file(file_path, file_name, "<your content goes here>")

    return await client.library.files.create(
        file_path=path,
        path=file_path,
    )


async def delete_file(client: AsyncAI21Client, file_id: str):
    await client.library.files.delete(file_id)


async def main():
    ai21_client = AsyncAI21Client(api_key="K8bU2iQWW0aqkUZwHdnFYgxjmMlge7QF")

    file_id = await upload_file(ai21_client)

    chat_response = await ai21_client.beta.conversational_rag.create(
        messages=messages,
        # you may add file IDs from your Studio library in order to question the model about their content
        file_ids=[file_id],
    )

    print("Chat Response:", chat_response)

    await delete_file(ai21_client, file_id)


if __name__ == "__main__":
    asyncio.run(main())
