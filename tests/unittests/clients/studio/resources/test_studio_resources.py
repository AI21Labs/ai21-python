from typing import TypeVar, Callable

import pytest
from ai21.http_client.http_client import AI21HTTPClient
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models.ai21_base_model import AI21BaseModel
from tests.unittests.clients.studio.resources.conftest import (
    get_studio_chat,
    get_studio_completion,
    get_chat_completions,
)

_BASE_URL = "https://test.api.ai21.com/studio/v1"
T = TypeVar("T", bound=StudioResource)


class TestStudioResources:
    @pytest.mark.parametrize(
        ids=[
            "studio_chat",
            "chat_completions",
            "studio_completion",
            "studio_completion_with_extra_args",
        ],
        argnames=[
            "studio_resource",
            "function_body",
            "url_suffix",
            "expected_body",
            "expected_httpx_response",
            "expected_response",
        ],
        argvalues=[
            (get_studio_chat()),
            (get_chat_completions()),
            (get_studio_completion(is_async=False)),
            (get_studio_completion(is_async=False, temperature=0.5, max_tokens=50)),
        ],
    )
    def test__create__should_return_response(
        self,
        studio_resource: Callable[[AI21HTTPClient], T],
        function_body,
        url_suffix: str,
        expected_body,
        expected_httpx_response,
        expected_response: AI21BaseModel,
        mock_ai21_studio_client: AI21HTTPClient,
    ):
        mock_ai21_studio_client.execute_http_request.return_value = expected_httpx_response

        resource = studio_resource(mock_ai21_studio_client)

        actual_response = resource.create(
            **function_body,
        )

        assert actual_response == expected_response
        mock_ai21_studio_client.execute_http_request.assert_called_with(
            method="POST",
            path=f"/{url_suffix}",
            body=expected_body,
            params={},
            stream=False,
            files=None,
        )
