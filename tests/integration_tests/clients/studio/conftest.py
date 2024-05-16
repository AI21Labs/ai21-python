import time
from pathlib import Path

import pytest

from ai21 import AI21Client

LIBRARY_FILE_TO_UPLOAD = str(Path(__file__).parent.parent / "resources" / "library_file.txt")
DEFAULT_LABELS = ["einstein", "science"]


def _wait_for_file_to_process(client: AI21Client, file_id: str, timeout: float = 60):
    start_time = time.time()

    elapsed_time = time.time() - start_time
    while elapsed_time < timeout:
        file_response = client.library.files.get(file_id)

        if file_response.status == "PROCESSED":
            return

        elapsed_time = time.time() - start_time
        time.sleep(0.5)

    raise TimeoutError(f"Timeout: {timeout} seconds passed. File processing not completed")


def _delete_uploaded_file(client: AI21Client, file_id: str):
    _wait_for_file_to_process(client, file_id)
    client.library.files.delete(file_id)


@pytest.fixture(scope="module")
def file_in_library():
    """
    Uploads a file to the library and deletes it after the test is done
    This happens in a scope of a module so the file is uploaded only once
    :return: file_id: str
    """
    client = AI21Client()

    # Delete any file that might be in the library due to failed tests
    files = client.library.files.list()
    for file in files:
        _delete_uploaded_file(client=client, file_id=file.file_id)

    file_id = client.library.files.create(file_path=LIBRARY_FILE_TO_UPLOAD, labels=DEFAULT_LABELS)
    _wait_for_file_to_process(client, file_id)
    yield file_id
    _delete_uploaded_file(client=client, file_id=file_id)
