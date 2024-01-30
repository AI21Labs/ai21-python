import time
from pathlib import Path

import pytest

from ai21 import AI21Client

LIBRARY_FILE_TO_UPLOAD = str(Path(__file__).parent.parent / "resources" / "library_file.txt")
DEFAULT_LABELS = ["einstein", "science"]


def _wait_for_file_to_process(client: AI21Client, file_id: str, timeout: float = 20):
    start_time = time.time()

    while True:
        file_response = client.library.files.get(file_id)

        if file_response.status == "PROCESSED":
            break

        elapsed_time = time.time() - start_time
        if elapsed_time >= timeout:
            raise TimeoutError(f"Timeout: {timeout} seconds passed. File processing not completed")

        time.sleep(0.5)


def _delete_file(client: AI21Client, file_id: str):
    _wait_for_file_to_process(client, file_id)
    client.library.files.delete(file_id)


@pytest.fixture(scope="module", autouse=True)
def handled_file():
    """
    Uploads a file to the library and deletes it after the test is done
    This happens in a scope of a module so the file is uploaded only once
    :return: file_id: str
    """
    client = AI21Client()

    file_id = client.library.files.create(file_path=LIBRARY_FILE_TO_UPLOAD, labels=DEFAULT_LABELS)
    _wait_for_file_to_process(client, file_id)
    yield file_id
    _delete_file(client, file_id=file_id)
