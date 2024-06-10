import asyncio
import os
import uuid

import file_utils
from ai21 import AsyncAI21Client, AI21APIError

# Use api_host for testing staging, default is production
# os.environ["AI21_API_HOST"] = "https://api-stage.ai21.com"

client = AsyncAI21Client()


def validate_file_deleted(file_id: str):
    try:
        client.library.files.get(file_id)
    except AI21APIError as e:
        print(f"File not found. Exception: {e.details}")


async def main():
    file_name = f"test-file3-{uuid.uuid4()}.txt"
    file_path = os.getcwd()

    path = os.path.join(file_path, file_name)
    _SOURCE_TEXT = """Holland is a geographical region and former province on the western coast of the
    Netherlands. From the 10th to the 16th century, Holland proper was  a unified political
     region within the Holy Roman Empire as a county ruled by the counts of Holland.
      By the 17th century, the province of Holland had risen to become a maritime and economic power,
       dominating the other provinces of the newly independent Dutch Republic."""
    file_utils.create_file(file_path, file_name, content=_SOURCE_TEXT)

    file_id = await client.library.files.create(
        file_path=path,
        path=file_path,
        labels=["label1", "label2"],
        public_url="www.example.com",
    )
    print(file_id)

    files = await client.library.files.list()
    print(files)
    uploaded_file = await client.library.files.get(file_id)
    print(uploaded_file)
    print(uploaded_file.name)
    print(uploaded_file.path)
    print(uploaded_file.labels)
    print(uploaded_file.public_url)

    await client.library.files.update(
        file_id,
        publicUrl="www.example-updated.com",
        labels=["label3", "label4"],
    )
    updated_file = await client.library.files.get(file_id)
    print(updated_file.name)
    print(updated_file.public_url)
    print(updated_file.labels)

    await client.library.files.delete(file_id)
    try:
        uploaded_file = await client.library.files.get(file_id)
    except AI21APIError as e:
        print(f"File not found. Exception: {e.details}")

    # Cleanup created file
    file_utils.delete_file(file_path, file_name)


asyncio.run(main())
