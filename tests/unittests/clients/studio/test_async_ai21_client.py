from ai21 import AI21Client, AI21EnvConfig


def test_ai21_client__when_pass_api_host__should_leave_as_is():
    base_url = "https://dont-modify-me.com"
    client = AI21Client(api_host=base_url)
    assert client._base_url == base_url


def test_ai21_client__when_not_pass_api_host__should_add_suffix():
    client = AI21Client()
    assert client._base_url == f"{AI21EnvConfig.api_host}/studio/v1"


def test_ai21_client__when_pass_ai21_api_host__should_add_suffix():
    ai21_url = "https://api.ai21.com"
    client = AI21Client(api_host=ai21_url)
    assert client._base_url == f"{ai21_url}/studio/v1"


def test_ai21_client__when_pass_ai21_with_suffix__should_not_modify():
    ai21_url = "https://api.ai21.com/studio/v1"
    client = AI21Client(api_host=ai21_url)
    assert client._base_url == ai21_url
