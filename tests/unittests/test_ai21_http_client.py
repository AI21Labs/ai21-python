import platform
from typing import Optional
from unittest.mock import Mock
from urllib.request import Request

import httpx
import pytest

from ai21.ai21_http_client import AI21HTTPClient
from ai21.http_client import HttpClient
from ai21.version import VERSION

_EXPECTED_USER_AGENT = (
    f"AI21 studio SDK {VERSION} Python {platform.python_version()} Operating System {platform.platform()}"
)

_DUMMY_API_KEY = "dummy_key"
_EXPECTED_GET_HEADERS = {
    "Authorization": "Bearer dummy_key",
    "Content-Type": "application/json",
    "User-Agent": _EXPECTED_USER_AGENT,
}

_EXPECTED_POST_FILE_HEADERS = {
    "Authorization": "Bearer dummy_key",
    "User-Agent": _EXPECTED_USER_AGENT,
}


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


@pytest.mark.parametrize(
    ids=[
        "when_pass_only_via__should_include_via_in_user_agent",
    ],
    argnames=["via", "expected_user_agent"],
    argvalues=[
        (
            "langchain",
            f"{_EXPECTED_USER_AGENT} via: langchain",
        ),
    ],
)
def test__build_headers__user_agent(via: Optional[str], expected_user_agent: str):
    client = AI21HTTPClient(api_key=_DUMMY_API_KEY, via=via)
    assert client._http_client._headers["User-Agent"] == expected_user_agent


def test__build_headers__authorization():
    client = AI21HTTPClient(api_key=_DUMMY_API_KEY)
    assert client._http_client._headers["Authorization"] == f"Bearer {_DUMMY_API_KEY}"


def test__build_headers__when_pass_headers__should_append():
    client = AI21HTTPClient(api_key=_DUMMY_API_KEY, headers={"foo": "bar"})
    assert client._http_client._headers["foo"] == "bar"
    assert client._http_client._headers["Authorization"] == f"Bearer {_DUMMY_API_KEY}"


@pytest.mark.parametrize(
    ids=[
        "when_making_request__should_send_appropriate_parameters",
        "when_making_request_with_files__should_send_appropriate_post_request",
    ],
    argnames=["params", "headers"],
    argvalues=[
        ({"method": "GET", "path": "/test_url", "params": {"foo": "bar"}, "body": {}}, _EXPECTED_GET_HEADERS),
        (
            {
                "method": "POST",
                "path": "/test_url",
                "body": {"foo": "bar"},
                "params": {},
                "stream": False,
                "files": {"file": "test_file"},
            },
            _EXPECTED_POST_FILE_HEADERS,
        ),
    ],
)
def test__execute_http_request__(
    params,
    headers,
    dummy_api_host: str,
    mock_httpx_client: httpx.Client,
):
    response_json = {"test_key": "test_value"}
    mock_response = Mock(spec=Request)
    mock_httpx_client.build_request.return_value = mock_response
    mock_httpx_client.send.return_value = MockResponse(response_json, 200)

    http_client = HttpClient(client=mock_httpx_client)
    client = AI21HTTPClient(http_client=http_client, api_key=_DUMMY_API_KEY, base_url=dummy_api_host, api_version="v1")

    response = client.execute_http_request(**params)
    assert response.json() == response_json

    if "files" in params:
        # We split it because when calling requests with "files", "params" is turned into "data"
        mock_httpx_client.build_request.assert_called_once_with(
            timeout=300,
            headers=headers,
            files=params["files"],
            data=params["body"],
            params=params["params"],
            url=f"{dummy_api_host}{params['path']}",
            method=params["method"],
        )
    else:
        mock_httpx_client.build_request.assert_called_once_with(
            timeout=300,
            headers=headers,
            url=f"{dummy_api_host}{params['path']}",
            params=params["params"],
            method=params["method"],
        )

    mock_httpx_client.send.assert_called_once_with(request=mock_response, stream=False)


def test__execute_http_request__when_files_with_put_method__should_raise_value_error(
    dummy_api_host: str,
    mock_httpx_client: httpx.Client,
):
    response_json = {"test_key": "test_value"}
    http_client = HttpClient(client=mock_httpx_client)
    client = AI21HTTPClient(http_client=http_client, api_key=_DUMMY_API_KEY, base_url=dummy_api_host, api_version="v1")

    mock_httpx_client.request.return_value = MockResponse(response_json, 200)
    with pytest.raises(ValueError):
        params = {"method": "PUT", "path": "test_url", "body": {"foo": "bar"}, "files": {"file": "test_file"}}
        client.execute_http_request(**params)
