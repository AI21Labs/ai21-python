from pathlib import Path
from time import sleep
import pytest

from ai21 import AI21Client, AsyncAI21Client
from tests.integration_tests.clients.studio.conftest import LIBRARY_FILE_TO_UPLOAD, DEFAULT_LABELS


def test_library__when_upload__should_get_file_id(file_in_library: str):
    assert file_in_library is not None


def test_library__when_list__should_get_file_id_in_list_of_files(file_in_library: str):
    client = AI21Client()

    files = client.library.files.list()
    assert files[0].file_id == file_in_library
    assert files[0].name == Path(LIBRARY_FILE_TO_UPLOAD).name


def test_library__when_get__should_match_file_id(file_in_library: str):
    client = AI21Client()

    file_response = client.library.files.get(file_in_library)
    assert file_response.file_id == file_in_library


def test_library__when_update__should_update_labels_successfully(file_in_library: str):
    client = AI21Client()

    file_response = client.library.files.get(file_in_library)
    assert set(file_response.labels) == set(DEFAULT_LABELS)
    sleep(2)

    new_labels = DEFAULT_LABELS + ["new_label"]
    client.library.files.update(file_in_library, labels=new_labels)
    file_response = client.library.files.get(file_in_library)
    assert set(file_response.labels) == set(new_labels)


@pytest.mark.asyncio
async def test_async_library__when_list__should_get_file_id_in_list_of_files(file_in_library: str):
    client = AsyncAI21Client()

    files = await client.library.files.list()
    assert files[0].file_id == file_in_library
    assert files[0].name == Path(LIBRARY_FILE_TO_UPLOAD).name


@pytest.mark.asyncio
async def test_async_library__when_get__should_match_file_id(file_in_library: str):
    client = AsyncAI21Client()

    file_response = await client.library.files.get(file_in_library)
    assert file_response.file_id == file_in_library


@pytest.mark.asyncio
async def test_async_library__when_update__should_update_labels_successfully(file_in_library: str):
    client = AsyncAI21Client()
    curr_labels = DEFAULT_LABELS + ["new_label"]
    file_response = await client.library.files.get(file_in_library)
    assert set(file_response.labels) == set(curr_labels)
    sleep(2)

    new_labels = curr_labels + ["new_label2"]
    await client.library.files.update(file_in_library, labels=new_labels)
    file_response = await client.library.files.get(file_in_library)
    print(file_response.labels)
    assert set(file_response.labels) == set(new_labels)
