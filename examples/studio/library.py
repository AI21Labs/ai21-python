import os
import uuid

import file_utils
from ai21 import AI21Client
from ai21.errors import APIError

# Use api_host for testing staging, default is production
# os.environ["AI21_API_HOST"] = "https://api-stage.ai21.com"

client = AI21Client()


def validate_file_deleted():
    try:
        client.library.files.get(file_id)
    except APIError as e:
        print(f"File not found. Exception: {e.details}")


file_name = f"test-file3-{uuid.uuid4()}.txt"
file_path = os.getcwd()

path = os.path.join(file_path, file_name)
file_utils.create_file(file_path, file_name, content="test content" * 100)


file_id = client.library.files.upload(
    file_path=path,
    path=file_path,
    labels=["label1", "label2"],
    public_url="www.example.com",
)
print(file_id)
files = client.library.files.list()
print(files)
uploaded_file = client.library.files.get(file_id)
print(uploaded_file)
print(uploaded_file.name)
print(uploaded_file.path)
print(uploaded_file.labels)
print(uploaded_file.public_url)

client.library.files.update(file_id, publicUrl="www.example-updated.com", labels=["label3", "label4"])
updated_file = client.library.files.get(file_id)
print(updated_file.name)
print(updated_file.public_url)
print(updated_file.labels)

client.library.files.delete(file_id)
try:
    uploaded_file = client.library.files.get(file_id)
except APIError as e:
    print(f"File not found. Exception: {e.details}")

# Cleanup created file
file_utils.delete_file(file_path, file_name)
