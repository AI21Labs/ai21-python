from typing import TypeVar, Callable

import pytest

from ai21 import AnswerResponse
from ai21.ai21_http_client import AI21HTTPClient
from ai21.clients.studio.resources.studio_answer import StudioAnswer
from ai21.clients.studio.resources.studio_resource import StudioResource
from tests.unittests.clients.studio.resources.conftest import get_studio_answer, get_studio_chat, get_studio_completion

_BASE_URL = "https://test.api.ai21.com/studio/v1"
_DUMMY_CONTEXT = "What is the answer to life, the universe and everything?"
_DUMMY_QUESTION = "What is the answer?"

T = TypeVar("T", bound=StudioResource)


class TestStudioResources:
    @pytest.mark.parametrize(
        ids=[
            "studio_answer",
            "studio_chat",
            "studio_completion",
        ],
        argnames=["studio_resource", "function_body", "url_suffix", "expected_body", "expected_response"],
        argvalues=[
            (get_studio_answer()),
            (get_studio_chat()),
            (get_studio_completion()),
        ],
    )
    def test__create__should_return_answer_response(
        self,
        studio_resource: Callable[[AI21HTTPClient], T],
        function_body,
        url_suffix: str,
        expected_body,
        expected_response,
        mock_ai21_studio_client: AI21HTTPClient,
    ):
        mock_ai21_studio_client.execute_http_request.return_value = expected_response.to_dict()
        mock_ai21_studio_client.get_base_url.return_value = _BASE_URL

        resource = studio_resource(mock_ai21_studio_client)

        actual_response = resource.create(
            **function_body,
        )

        assert actual_response == expected_response
        mock_ai21_studio_client.execute_http_request.assert_called_with(
            method="POST",
            url=f"{_BASE_URL}/{url_suffix}",
            params=expected_body,
            files=None,
        )

    def test__create__when_pass_kwargs__should_not_pass_to_request(self, mock_ai21_studio_client: AI21HTTPClient):
        expected_answer = AnswerResponse(id="some-id", answer_in_context=True, answer="42")
        mock_ai21_studio_client.execute_http_request.return_value = expected_answer.to_dict()
        mock_ai21_studio_client.get_base_url.return_value = _BASE_URL
        studio_answer = StudioAnswer(mock_ai21_studio_client)

        studio_answer.create(
            context=_DUMMY_CONTEXT,
            question=_DUMMY_QUESTION,
            some_dummy_kwargs="some_dummy_value",
        )

        mock_ai21_studio_client.execute_http_request.assert_called_with(
            method="POST",
            url=_BASE_URL + "/answer",
            params={
                "answerLength": None,
                "context": _DUMMY_CONTEXT,
                "mode": None,
                "question": _DUMMY_QUESTION,
            },
            files=None,
        )
