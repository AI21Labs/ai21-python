import json
from unittest.mock import patch
import pytest

import httpx

from ai21 import AI21Client, AsyncAI21Client
from ai21.models.chat import ChatMessage, ChatCompletionResponse, ChatCompletionChunk, ChoicesChunk, ChoiceDelta
from ai21.models import RoleType

_MODEL = "jamba-instruct-preview"
_MESSAGES = [
    ChatMessage(
        content="Hello, I need help studying for the coming test, can you teach me about the US constitution? ",
        role=RoleType.USER,
    ),
]

_BAD_HTTPX_REQUEST = httpx.Request(method="POST", url="http://test_url")
_BAD_HTTPX_RESPONSE = httpx.Response(status_code=500, request=_BAD_HTTPX_REQUEST)
_EXPECTED_MESSAGE_CONTENT = {
    "id": "test",
    "choices": [
        {"index": 0, "message": {"content": "test", "role": "assistant"}, "finish_reason": None, "logprobs": None}
    ],
    "usage": {"prompt_tokens": 1, "total_tokens": 2, "completion_tokens": 1},
}


def test_chat_completion():
    messages = _MESSAGES

    client = AI21Client()
    response = client.chat.completions.create(
        model=_MODEL,
        messages=messages,
        max_tokens=64,
        temperature=0.7,
        stop=["\n"],
        top_p=0.3,
    )

    assert isinstance(response, ChatCompletionResponse)
    assert response.choices[0].message.content
    assert response.choices[0].message.role


def test_chat_completion_when_num_retries_is_over_1__should_retry():
    num_retries = 3

    with patch.object(
        httpx.Client,
        "send",
        side_effect=[
            _BAD_HTTPX_RESPONSE,
            _BAD_HTTPX_RESPONSE,
            httpx.Response(status_code=200, content=json.dumps(_EXPECTED_MESSAGE_CONTENT)),
        ],
    ) as mock_send:
        messages = _MESSAGES

        client = AI21Client(num_retries=num_retries)
        response = client.chat.completions.create(
            model=_MODEL,
            messages=messages,
        )

        assert isinstance(response, ChatCompletionResponse)
        assert mock_send.call_count == num_retries


def test_chat_completion__with_n_param__should_return_n_choices():
    messages = _MESSAGES
    n = 3

    client = AI21Client()
    response = client.chat.completions.create(
        model=_MODEL,
        messages=messages,
        max_tokens=64,
        temperature=0.7,
        stop=["\n"],
        top_p=0.3,
        n=n,
    )

    assert isinstance(response, ChatCompletionResponse)
    assert len(response.choices) == n
    for choice in response.choices:
        assert choice.message.content
        assert choice.message.role


def test_chat_completion__when_stream__should_return_chunks():
    messages = _MESSAGES

    client = AI21Client()

    response = client.chat.completions.create(
        model=_MODEL,
        messages=messages,
        temperature=0,
        stream=True,
    )

    for chunk in response:
        assert isinstance(chunk, ChatCompletionChunk)
        assert isinstance(chunk.choices[0], ChoicesChunk)
        assert isinstance(chunk.choices[0].delta, ChoiceDelta)


@pytest.mark.asyncio
async def test_async_chat_completion():
    messages = _MESSAGES

    client = AsyncAI21Client()
    response = await client.chat.completions.create(
        model=_MODEL,
        messages=messages,
        max_tokens=64,
        temperature=0.7,
        stop=["\n"],
        top_p=0.3,
    )

    assert isinstance(response, ChatCompletionResponse)
    assert response.choices[0].message.content
    assert response.choices[0].message.role


@pytest.mark.asyncio
async def test_async_chat_completion__when_stream__should_return_chunks():
    messages = _MESSAGES

    client = AsyncAI21Client()

    response = await client.chat.completions.create(
        model=_MODEL,
        messages=messages,
        temperature=0,
        stream=True,
    )

    async for chunk in response:
        assert isinstance(chunk, ChatCompletionChunk)
        assert isinstance(chunk.choices[0], ChoicesChunk)
        assert isinstance(chunk.choices[0].delta, ChoiceDelta)


@pytest.mark.asyncio
async def test_async_chat_completion_when_num_retries_is_over_1__should_retry():
    num_retries = 3

    with patch.object(
        httpx.AsyncClient,
        "send",
        side_effect=[
            _BAD_HTTPX_RESPONSE,
            _BAD_HTTPX_RESPONSE,
            httpx.Response(status_code=200, content=json.dumps(_EXPECTED_MESSAGE_CONTENT)),
        ],
    ) as mock_send:
        messages = _MESSAGES

        client = AsyncAI21Client(num_retries=num_retries)
        response = await client.chat.completions.create(
            model=_MODEL,
            messages=messages,
        )

        assert isinstance(response, ChatCompletionResponse)
        assert mock_send.call_count == num_retries


@pytest.mark.asyncio
async def test_async_chat_completion__with_n_param__should_return_n_choices():
    messages = _MESSAGES
    n = 3

    client = AsyncAI21Client()
    response = await client.chat.completions.create(
        model=_MODEL,
        messages=messages,
        max_tokens=64,
        temperature=0.7,
        stop=["\n"],
        top_p=0.3,
        n=n,
    )

    assert isinstance(response, ChatCompletionResponse)
    assert len(response.choices) == n
    for choice in response.choices:
        assert choice.message.content
        assert choice.message.role
