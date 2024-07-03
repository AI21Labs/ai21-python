import pytest
from ai21 import AsyncAI21Client, AI21EnvConfig


@pytest.mark.asyncio
def test_async_ai21_client__when_pass_api_host__should_leave_as_is():
    base_url = "https://dont-modify-me.com"
    client = AsyncAI21Client(api_host=base_url)
    assert client._base_url == base_url


@pytest.mark.asyncio
def test_async_ai21_client__when_not_pass_api_host__should_add_suffix():
    client = AsyncAI21Client()
    assert client._base_url == f"{AI21EnvConfig.api_host}/studio/v1"


@pytest.mark.asyncio
def test_async_ai21_client__when_pass_ai21_api_host__should_add_suffix():
    ai21_url = "https://api.ai21.com"
    client = AsyncAI21Client(api_host=ai21_url)
    assert client._base_url == f"{ai21_url}/studio/v1"


@pytest.mark.asyncio
def test_async_ai21_client__when_pass_ai21_with_suffix__should_not_modify():
    ai21_url = "https://api.ai21.com/studio/v1"
    client = AsyncAI21Client(api_host=ai21_url)
    assert client._base_url == ai21_url
