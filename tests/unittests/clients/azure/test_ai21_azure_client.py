import pytest

from ai21 import AI21AzureClient


def test__when_with_api_key__should_be_ok():
    client = AI21AzureClient(base_url="https://example.com", api_key="test_api_key")
    assert client._api_key == "test_api_key"
    assert client._azure_ad_token is None
    assert client._azure_ad_token_provider is None


def test__when_with_azure_ad_token__should_be_ok():
    client = AI21AzureClient(base_url="https://example.com", azure_ad_token="test_azure_ad_token")
    assert client._azure_ad_token == "test_azure_ad_token"
    assert client._api_key is None
    assert client._azure_ad_token_provider is None


def test__when_with_azure_ad_token_provider__should_be_ok():
    def token_provider():
        return "test_azure_ad_token"

    client = AI21AzureClient(base_url="https://example.com", azure_ad_token_provider=token_provider)
    assert client._azure_ad_token_provider == token_provider
    assert client._api_key is None
    assert client._azure_ad_token is None


def test__when_without_any_token_or_key__should_raise_error():
    with pytest.raises(ValueError, match="Must provide either api_key or azure_ad_token_provider or azure_ad_token"):
        AI21AzureClient(base_url="https://example.com")
