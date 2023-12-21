from typing import Optional

import pytest

from ai21.ai21_http_client import AI21HTTPClient
from ai21.version import VERSION

_DUMMY_API_KEY = "dummy_key"


class TestAI21StudioClient:
    @pytest.mark.parametrize(
        ids=[
            "when_pass_only_via__should_include_via_in_user_agent",
            "when_pass_only_application__should_include_application_in_user_agent",
            "when_pass_organization__should_include_organization_in_user_agent",
            "when_pass_all_user_agent_relevant_params__should_include_them_in_user_agent",
        ],
        argnames=["via", "application", "organization", "expected_user_agent"],
        argvalues=[
            ("langchain", None, None, f"ai21 studio SDK {VERSION} via: langchain"),
            (None, "studio", None, f"ai21 studio SDK {VERSION} application: studio"),
            (None, None, "ai21", f"ai21 studio SDK {VERSION} organization: ai21"),
            (
                "langchain",
                "studio",
                "ai21",
                f"ai21 studio SDK {VERSION} organization: ai21 application: studio via: langchain",
            ),
        ],
    )
    def test__build_headers__user_agent(
        self, via: Optional[str], application: Optional[str], organization: Optional[str], expected_user_agent: str
    ):
        client = AI21HTTPClient(api_key=_DUMMY_API_KEY, via=via, application=application, organization=organization)
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
            "when_api_host_is_not_set__should_return_default",
            "when_api_host_is_set__should_return_set_value",
        ],
        argnames=["api_host", "expected_api_host"],
        argvalues=[
            (None, "https://api.ai21.com/studio/v1"),
            ("http://test_host", "http://test_host/studio/v1"),
        ],
    )
    def test__get_base_url(self, api_host: Optional[str], expected_api_host: str):
        client = AI21HTTPClient(api_key=_DUMMY_API_KEY, api_host=api_host, api_version="v1")
        assert client.get_base_url() == expected_api_host
