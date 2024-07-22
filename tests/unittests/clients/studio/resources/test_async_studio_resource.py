from typing import TypeVar, Callable

import pytest
import httpx
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.clients.studio.resources.studio_answer import AsyncStudioAnswer
from ai21.clients.studio.resources.studio_resource import AsyncStudioResource
from ai21.models import AnswerResponse
from tests.unittests.clients.studio.resources.conftest import (
    get_studio_answer,
    get_studio_chat,
    get_chat_completions,
    get_studio_completion,
    get_studio_embed,
    get_studio_gec,
    get_studio_improvements,
    get_studio_paraphrase,
    get_studio_segmentation,
    get_studio_summarization,
    get_studio_summarize_by_segment,
)

_BASE_URL = "https://test.api.ai21.com/studio/v1"
_DUMMY_CONTEXT = "What is the answer to life, the universe and everything?"
_DUMMY_QUESTION = "What is the answer?"

T = TypeVar("T", bound=AsyncStudioResource)


class TestAsyncStudioResources:
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        ids=[
            "async_studio_answer",
            "async_studio_chat",
            "async_chat_completions",
            "async_studio_completion",
            "async_studio_completion_with_extra_args",
            "async_studio_embed",
            "async_studio_gec",
            "async_studio_improvements",
            "async_studio_paraphrase",
            "async_studio_segmentation",
            "async_studio_summarization",
            "async_studio_summarize_by_segment",
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
            (get_studio_answer(is_async=True)),
            (get_studio_chat(is_async=True)),
            (get_chat_completions(is_async=True)),
            (get_studio_completion(is_async=True)),
            (get_studio_completion(is_async=True, temperature=0.5, max_tokens=50)),
            (get_studio_embed(is_async=True)),
            (get_studio_gec(is_async=True)),
            (get_studio_improvements(is_async=True)),
            (get_studio_paraphrase(is_async=True)),
            (get_studio_segmentation(is_async=True)),
            (get_studio_summarization(is_async=True)),
            (get_studio_summarize_by_segment(is_async=True)),
        ],
    )
    async def test__create__should_return_response(
        self,
        studio_resource: Callable[[AsyncAI21HTTPClient], T],
        function_body,
        url_suffix: str,
        expected_body,
        expected_httpx_response,
        expected_response: AnswerResponse,
        mock_async_ai21_studio_client: AsyncAI21HTTPClient,
    ):
        mock_async_ai21_studio_client.execute_http_request.return_value = expected_httpx_response

        resource = studio_resource(mock_async_ai21_studio_client)

        actual_response = await resource.create(
            **function_body,
        )

        assert actual_response == expected_response
        mock_async_ai21_studio_client.execute_http_request.assert_called_with(
            method="POST",
            path=f"/{url_suffix}",
            body=expected_body,
            params={},
            stream=False,
            files=None,
        )

    @pytest.mark.asyncio
    async def test__create__when_pass_kwargs__should_pass_to_request(
        self,
        mock_async_ai21_studio_client: AsyncAI21HTTPClient,
        mock_async_successful_httpx_response: httpx.Response,
    ):
        expected_answer = AnswerResponse(id="some-id", answer_in_context=True, answer="42")
        mock_async_successful_httpx_response.json.return_value = expected_answer.to_dict()

        mock_async_ai21_studio_client.execute_http_request.return_value = mock_async_successful_httpx_response
        studio_answer = AsyncStudioAnswer(mock_async_ai21_studio_client)

        await studio_answer.create(
            context=_DUMMY_CONTEXT,
            question=_DUMMY_QUESTION,
            some_dummy_kwargs="some_dummy_value",
        )

        mock_async_ai21_studio_client.execute_http_request.assert_called_with(
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
