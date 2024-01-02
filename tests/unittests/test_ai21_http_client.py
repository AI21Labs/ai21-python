from typing import Optional

import pytest
import requests

from ai21.ai21_http_client import AI21HTTPClient
from ai21.http_client import HttpClient
from ai21.version import VERSION

_DUMMY_API_KEY = "dummy_key"
_EXPECTED_GET_HEADERS = {
    "Authorization": "Bearer dummy_key",
    "Content-Type": "application/json",
    "User-Agent": f"ai21 studio SDK {VERSION}",
}

_EXPECTED_POST_FILE_HEADERS = {
    "Authorization": "Bearer dummy_key",
    "User-Agent": f"ai21 studio SDK {VERSION}",
}


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


class TestAI21StudioClient:
    @pytest.mark.parametrize(
        ids=[
            "when_pass_only_via__should_include_via_in_user_agent",
        ],
        argnames=["via", "expected_user_agent"],
        argvalues=[
            ("langchain", f"ai21 studio SDK {VERSION} via: langchain"),
        ],
    )
    def test__build_headers__user_agent(self, via: Optional[str], expected_user_agent: str):
        client = AI21HTTPClient(api_key=_DUMMY_API_KEY, via=via)
        assert client._http_client._headers["User-Agent"] == expected_user_agent

    def test__build_headers__authorization(self):
        client = AI21HTTPClient(api_key=_DUMMY_API_KEY)
        assert client._http_client._headers["Authorization"] == f"Bearer {_DUMMY_API_KEY}"

    def test__build_headers__when_pass_headers__should_append(self):
        client = AI21HTTPClient(api_key=_DUMMY_API_KEY, headers={"foo": "bar"})
        assert client._http_client._headers["foo"] == "bar"
        assert client._http_client._headers["Authorization"] == f"Bearer {_DUMMY_API_KEY}"

    @pytest.mark.parametrize(
        ids=[
            "when_api_host_is_set__should_return_set_value",
        ],
        argnames=["api_host", "expected_api_host"],
        argvalues=[
            ("http://test_host", "http://test_host/studio/v1"),
        ],
    )
    def test__get_base_url(self, api_host: Optional[str], expected_api_host: str):
        client = AI21HTTPClient(api_key=_DUMMY_API_KEY, api_host=api_host, api_version="v1")
        assert client.get_base_url() == expected_api_host

    @pytest.mark.parametrize(
        ids=[
            "when_making_request__should_send_appropriate_parameters",
            "when_making_request_with_files__should_send_appropriate_post_request",
        ],
        argnames=["params", "headers"],
        argvalues=[
            ({"method": "GET", "url": "test_url", "params": {"foo": "bar"}}, _EXPECTED_GET_HEADERS),
            (
                {"method": "POST", "url": "test_url", "params": {"foo": "bar"}, "files": {"file": "test_file"}},
                _EXPECTED_POST_FILE_HEADERS,
            ),
        ],
    )
    def test__execute_http_request__(
        self,
        params,
        headers,
        dummy_api_host: str,
        mock_requests_session: requests.Session,
    ):
        response_json = {"test_key": "test_value"}
        mock_requests_session.request.return_value = MockResponse(response_json, 200)

        http_client = HttpClient(session=mock_requests_session)
        client = AI21HTTPClient(
            http_client=http_client, api_key=_DUMMY_API_KEY, api_host=dummy_api_host, api_version="v1"
        )

        response = client.execute_http_request(**params)
        assert response == response_json

        if "files" in params:
            # We split it because when calling requests with "files", "params" is turned into "data"
            mock_requests_session.request.assert_called_once_with(
                timeout=300,
                headers=headers,
                files=params["files"],
                data=params["params"],
                url=params["url"],
                method=params["method"],
            )
        else:
            mock_requests_session.request.assert_called_once_with(timeout=300, headers=headers, **params)

    def test__execute_http_request__when_files_with_put_method__should_raise_value_error(
        self,
        dummy_api_host: str,
        mock_requests_session: requests.Session,
    ):
        response_json = {"test_key": "test_value"}
        http_client = HttpClient(session=mock_requests_session)
        client = AI21HTTPClient(
            http_client=http_client, api_key=_DUMMY_API_KEY, api_host=dummy_api_host, api_version="v1"
        )

        mock_requests_session.request.return_value = MockResponse(response_json, 200)
        with pytest.raises(ValueError):
            params = {"method": "PUT", "url": "test_url", "params": {"foo": "bar"}, "files": {"file": "test_file"}}
            client.execute_http_request(**params)
