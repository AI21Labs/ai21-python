from typing import TypeVar, Callable

import pytest
import httpx
from ai21.http_client.http_client import AI21HTTPClient
from ai21.clients.studio.resources.studio_answer import StudioAnswer
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models import AnswerResponse
from tests.unittests.clients.studio.resources.conftest import (
    get_studio_answer,
    get_studio_chat,
    get_studio_completion,
    get_studio_embed,
    get_studio_gec,
    get_studio_improvements,
    get_studio_paraphrase,
    get_studio_segmentation,
    get_studio_summarization,
    get_studio_summarize_by_segment,
    get_chat_completions,
)

_BASE_URL = "https://test.api.ai21.com/studio/v1"
_DUMMY_CONTEXT = "What is the answer to life, the universe and everything?"
_DUMMY_QUESTION = "What is the answer?"

T = TypeVar("T", bound=StudioResource)


class TestStudioResources:
    @pytest.mark.parametrize(
        ids=[
            "studio_answer",
            "studio_chat",
            "chat_completions",
            "studio_completion",
            "studio_completion_with_extra_args",
            "studio_embed",
            "studio_gec",
            "studio_improvements",
            "studio_paraphrase",
            "studio_segmentation",
            "studio_summarization",
            "studio_summarize_by_segment",
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
            (get_studio_answer()),
            (get_studio_chat()),
            (get_chat_completions()),
            (get_studio_completion(is_async=False)),
            (get_studio_completion(is_async=False, temperature=0.5, max_tokens=50)),
            (get_studio_embed()),
            (get_studio_gec()),
            (get_studio_improvements()),
            (get_studio_paraphrase()),
            (get_studio_segmentation()),
            (get_studio_summarization()),
            (get_studio_summarize_by_segment()),
        ],
    )
    def test__create__should_return_response(
        self,
        studio_resource: Callable[[AI21HTTPClient], T],
        function_body,
        url_suffix: str,
        expected_body,
        expected_httpx_response,
        expected_response: AnswerResponse,
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

    def test__create__when_pass_kwargs__should_pass_to_request(
        self,
        mock_ai21_studio_client: AI21HTTPClient,
        mock_successful_httpx_response: httpx.Response,
    ):
        expected_answer = AnswerResponse(id="some-id", answer_in_context=True, answer="42")
        mock_successful_httpx_response.json.return_value = expected_answer.to_dict()

        mock_ai21_studio_client.execute_http_request.return_value = mock_successful_httpx_response
        studio_answer = StudioAnswer(mock_ai21_studio_client)

        studio_answer.create(
            context=_DUMMY_CONTEXT,
            question=_DUMMY_QUESTION,
            some_dummy_kwargs="some_dummy_value",
        )

        mock_ai21_studio_client.execute_http_request.assert_called_with(
            method="POST",
            path="/answer",
            body={
                "context": _DUMMY_CONTEXT,
                "question": _DUMMY_QUESTION,
                "some_dummy_kwargs": "some_dummy_value",
            },
            params={},
            stream=False,
            files=None,
        )
