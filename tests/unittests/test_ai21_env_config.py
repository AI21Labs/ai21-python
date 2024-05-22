import os
from ai21 import AI21Client

_FAKE_API_KEY = "fake-key"
os.environ["AI21_API_KEY"] = _FAKE_API_KEY


def test_env_config__when_set_twice__should_be_updated():
    client = AI21Client()

    assert client._http_client._api_key == _FAKE_API_KEY

    new_api_key = "new-key"
    os.environ["AI21_API_KEY"] = new_api_key
    client2 = AI21Client()
    assert client2._http_client._api_key == new_api_key


def test_env_config__when_set_via_init_and_env__should_be_taken_from_init():
    client = AI21Client()
    assert client._http_client._api_key == _FAKE_API_KEY

    init_api_key = "init-key"
    client2 = AI21Client(api_key=init_api_key)

    assert client2._http_client._api_key == init_api_key


def test_env_config__when_set_int__should_be_set():
    os.environ["AI21_TIMEOUT_SEC"] = "1"

    client = AI21Client()

    assert client._http_client._timeout_sec == 1
