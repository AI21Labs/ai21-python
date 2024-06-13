from ai21 import AI21Client, AI21EnvConfig


def test_ai21_client__when_pass_api_host__should_leave_as_is():
    base_url = "https://dont-modify-me.com"
    client = AI21Client(api_host=base_url)
    assert client._http_client._base_url == base_url


def test_ai21_client__when_not_pass_api_host__should_add_suffix():
    client = AI21Client()
    assert client._http_client._base_url == f"{AI21EnvConfig.api_host}/studio/v1"
