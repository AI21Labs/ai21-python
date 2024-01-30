from pathlib import Path
from time import sleep

from ai21 import AI21Client
from tests.integration_tests.clients.studio.conftest import LIBRARY_FILE_TO_UPLOAD, DEFAULT_LABELS


def test_library__when_upload__should_get_file_id(handled_file: str):
    assert handled_file is not None


def test_library__when_list__should_get_file_id_in_list_of_files(handled_file: str):
    client = AI21Client()

    files = client.library.files.list()
    assert handled_file in [file.file_id for file in files]
    assert Path(LIBRARY_FILE_TO_UPLOAD).name in [file.name for file in files]


def test_library__when_get__should_match_file_id(handled_file: str):
    client = AI21Client()

    file_response = client.library.files.get(handled_file)
    assert file_response.file_id == handled_file


def test_library__when_update__should_update_labels_successfully(handled_file: str):
    client = AI21Client()

    file_response = client.library.files.get(handled_file)
    assert set(file_response.labels) == set(DEFAULT_LABELS)
    sleep(2)

    new_labels = DEFAULT_LABELS + ["new_label"]
    client.library.files.update(handled_file, labels=new_labels)
    file_response = client.library.files.get(handled_file)
    assert set(file_response.labels) == set(new_labels)
