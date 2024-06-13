import pytest

from ai21 import AI21AzureClient


def test__azure_client__when_init_with_no_auth__should_raise_error():
    with pytest.raises(ValueError) as e:
        AI21AzureClient(base_url="http://some_endpoint_url")

    assert str(e.value) == "Must provide either api_key or azure_ad_token_provider or azure_ad_token"
