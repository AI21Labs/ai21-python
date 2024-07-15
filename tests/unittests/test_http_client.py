import pytest
from unittest.mock import Mock
from urllib.request import Request

import httpx

from ai21.errors import ServiceUnavailable
from ai21.http_client.base_http_client import RETRY_ERROR_CODES
from ai21.http_client.http_client import AI21HTTPClient
from ai21.http_client.async_http_client import AsyncAI21HTTPClient

_METHOD = "GET"
_URL = "http://test_url"
_API_KEY = "fake-key"


def test__execute_http_request__when_retry_error_code_once__should_retry_and_succeed(mock_httpx_client: Mock) -> None:
    request = Request(method=_METHOD, url=_URL)
    retries = 3
    mock_httpx_client.send.side_effect = [
        httpx.Response(status_code=429, request=request),
        httpx.Response(status_code=200, request=request, json={"test_key": "test_value"}),
    ]

    client = AI21HTTPClient(client=mock_httpx_client, num_retries=retries, base_url=_URL, api_key=_API_KEY)
    client.execute_http_request(method=_METHOD)
    assert mock_httpx_client.send.call_count == retries - 1


def test__execute_http_request__when_retry_error__should_retry_and_stop(mock_httpx_client: Mock) -> None:
    request = Request(method=_METHOD, url=_URL)
    retries = len(RETRY_ERROR_CODES)

    mock_httpx_client.send.side_effect = [
        httpx.Response(status_code=status_code, request=request) for status_code in RETRY_ERROR_CODES
    ]

    client = AI21HTTPClient(client=mock_httpx_client, num_retries=retries, base_url=_URL, api_key=_API_KEY)
    with pytest.raises(ServiceUnavailable):
        client.execute_http_request(method=_METHOD)

    assert mock_httpx_client.send.call_count == retries


@pytest.mark.asyncio
async def test__execute_async_http_request__when_retry_error_code_once__should_retry_and_succeed(
    mock_httpx_async_client: Mock,
) -> None:
    request = Request(method=_METHOD, url=_URL)
    retries = 3
    mock_httpx_async_client.send.side_effect = [
        httpx.Response(status_code=429, request=request),
        httpx.Response(status_code=200, request=request, json={"test_key": "test_value"}),
    ]

    client = AsyncAI21HTTPClient(client=mock_httpx_async_client, num_retries=retries, base_url=_URL, api_key=_API_KEY)
    await client.execute_http_request(method=_METHOD)
    assert mock_httpx_async_client.send.call_count == retries - 1


@pytest.mark.asyncio
async def test__execute_async_http_request__when_retry_error__should_retry_and_stop(
    mock_httpx_async_client: Mock,
) -> None:
    request = Request(method=_METHOD, url=_URL)
    retries = len(RETRY_ERROR_CODES)

    mock_httpx_async_client.send.side_effect = [
        httpx.Response(status_code=status_code, request=request) for status_code in RETRY_ERROR_CODES
    ]

    client = AsyncAI21HTTPClient(client=mock_httpx_async_client, num_retries=retries, base_url=_URL, api_key=_API_KEY)
    with pytest.raises(ServiceUnavailable):
        await client.execute_http_request(method=_METHOD)

    assert mock_httpx_async_client.send.call_count == retries
