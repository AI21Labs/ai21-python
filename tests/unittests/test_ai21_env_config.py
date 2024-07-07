import os
from contextlib import contextmanager

from ai21 import AI21Client

_FAKE_API_KEY = "fake-key"
os.environ["AI21_API_KEY"] = _FAKE_API_KEY


@contextmanager
def set_env_var(key: str, value: str):
    os.environ[key] = value
    yield
    del os.environ[key]


def test_env_config__when_set_via_init_and_env__should_be_taken_from_init():
    client = AI21Client()
    assert client._api_key == _FAKE_API_KEY

    init_api_key = "init-key"
    client2 = AI21Client(api_key=init_api_key)

    assert client2._api_key == init_api_key


def test_env_config__when_set_twice__should_be_updated():
    client = AI21Client()

    assert client._api_key == _FAKE_API_KEY

    new_api_key = "new-key"

    with set_env_var("AI21_API_KEY", new_api_key):
        client2 = AI21Client()
        assert client2._api_key == new_api_key


def test_env_config__when_set_int__should_be_set():
    with set_env_var("AI21_TIMEOUT_SEC", "1"):
        client = AI21Client()

        assert client._timeout_sec == 1
