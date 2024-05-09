import pytest
from unittest.mock import Mock
from urllib.request import Request

import httpx

from ai21.errors import ServiceUnavailable
from ai21.http_client import HttpClient, RETRY_ERROR_CODES

_METHOD = "GET"
_URL = "http://test_url"


def test__execute_http_request__when_retry_error_code_once__should_retry_and_succeed(mock_httpx_client: Mock) -> None:
    request = Request(method=_METHOD, url=_URL)
    retries = 3
    mock_httpx_client.request.side_effect = [
        httpx.Response(status_code=429, request=request),
        httpx.Response(status_code=200, request=request, json={"test_key": "test_value"}),
    ]

    client = HttpClient(client=mock_httpx_client, num_retries=retries)
    client.execute_http_request(method=_METHOD, url=_URL)
    assert mock_httpx_client.request.call_count == retries - 1


def test__execute_http_request__when_retry_error__should_retry_and_stop(mock_httpx_client: Mock) -> None:
    request = Request(method=_METHOD, url=_URL)
    retries = len(RETRY_ERROR_CODES)

    mock_httpx_client.request.side_effect = [
        httpx.Response(status_code=status_code, request=request) for status_code in RETRY_ERROR_CODES
    ]

    client = HttpClient(client=mock_httpx_client, num_retries=retries)
    with pytest.raises(ServiceUnavailable):
        client.execute_http_request(method=_METHOD, url=_URL)

    assert mock_httpx_client.request.call_count == retries
