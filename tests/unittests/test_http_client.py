from unittest.mock import Mock

import httpx
import pytest

from ai21.errors import ServiceUnavailable, Unauthorized
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.base_http_client import RETRY_ERROR_CODES
from ai21.http_client.http_client import AI21HTTPClient

_METHOD = "GET"
_URL = "http://test_url"
_API_KEY = "fake-key"


def test__execute_http_request__when_retry_error_code_once__should_retry_and_succeed(mock_httpx_client: Mock) -> None:
    request = httpx.Request(method=_METHOD, url=_URL)
    retries = 3
    mock_httpx_client.send.side_effect = [
        httpx.Response(status_code=429, request=request),
        httpx.Response(status_code=200, request=request, json={"test_key": "test_value"}),
    ]

    client = AI21HTTPClient(client=mock_httpx_client, num_retries=retries, base_url=_URL, api_key=_API_KEY)
    client.execute_http_request(method=_METHOD)
    assert mock_httpx_client.send.call_count == retries - 1


def test__execute_http_request__when_retry_error__should_retry_and_stop(mock_httpx_client: Mock) -> None:
    request = httpx.Request(method=_METHOD, url=_URL)
    retries = len(RETRY_ERROR_CODES)

    mock_httpx_client.send.side_effect = [
        httpx.Response(status_code=status_code, request=request) for status_code in RETRY_ERROR_CODES
    ]

    client = AI21HTTPClient(client=mock_httpx_client, num_retries=retries, base_url=_URL, api_key=_API_KEY)
    with pytest.raises(ServiceUnavailable):
        client.execute_http_request(method=_METHOD)

    assert mock_httpx_client.send.call_count == retries


def test__execute_http_request__when_streaming__should_handle_non_200_response_code(mock_httpx_client: Mock) -> None:
    error_details = "test_error"
    request = httpx.Request(method=_METHOD, url=_URL)
    response = httpx.Response(status_code=401, request=request, text=error_details)
    mock_httpx_client.send.return_value = response

    client = AI21HTTPClient(client=mock_httpx_client, base_url=_URL, api_key=_API_KEY)
    with pytest.raises(Unauthorized, match=error_details):
        client.execute_http_request(method=_METHOD, stream=True)


@pytest.mark.asyncio
async def test__execute_async_http_request__when_retry_error_code_once__should_retry_and_succeed(
    mock_httpx_async_client: Mock,
) -> None:
    request = httpx.Request(method=_METHOD, url=_URL)
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
    request = httpx.Request(method=_METHOD, url=_URL)
    retries = len(RETRY_ERROR_CODES)

    mock_httpx_async_client.send.side_effect = [
        httpx.Response(status_code=status_code, request=request) for status_code in RETRY_ERROR_CODES
    ]

    client = AsyncAI21HTTPClient(client=mock_httpx_async_client, num_retries=retries, base_url=_URL, api_key=_API_KEY)
    with pytest.raises(ServiceUnavailable):
        await client.execute_http_request(method=_METHOD)

    assert mock_httpx_async_client.send.call_count == retries


@pytest.mark.asyncio
async def test__execute_async_http_request__when_streaming__should_handle_non_200_response_code(
    mock_httpx_async_client: Mock,
) -> None:
    error_details = "test_error"
    request = httpx.Request(method=_METHOD, url=_URL)
    response = httpx.Response(status_code=401, request=request, text=error_details)
    mock_httpx_async_client.send.return_value = response

    client = AsyncAI21HTTPClient(client=mock_httpx_async_client, base_url=_URL, api_key=_API_KEY)
    with pytest.raises(Unauthorized, match=error_details):
        await client.execute_http_request(method=_METHOD, stream=True)
