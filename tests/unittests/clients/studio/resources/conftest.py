import httpx
import pytest
from pytest_mock import MockerFixture

from ai21.clients.studio.resources.chat import AsyncChatCompletions
from ai21.clients.studio.resources.chat import ChatCompletions
from ai21.clients.studio.resources.studio_chat import StudioChat, AsyncStudioChat
from ai21.clients.studio.resources.studio_completion import StudioCompletion, AsyncStudioCompletion
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models import (
    ChatMessage,
    RoleType,
    ChatResponse,
    CompletionsResponse,
)
from ai21.models._pydantic_compatibility import _to_dict, _from_dict
from ai21.models.chat import (
    ChatMessage as ChatCompletionChatMessage,
    ChatCompletionResponse,
)
from ai21.utils.typing import to_lower_camel_case


@pytest.fixture
def mock_ai21_studio_client(mocker: MockerFixture) -> AI21HTTPClient:
    return mocker.MagicMock(spec=AI21HTTPClient)


@pytest.fixture
def mock_async_ai21_studio_client(mocker: MockerFixture) -> AsyncAI21HTTPClient:
    return mocker.MagicMock(spec=AsyncAI21HTTPClient)


@pytest.fixture
def mock_successful_httpx_response(mocker: MockerFixture) -> httpx.Response:
    mock_httpx_response = mocker.Mock(spec=httpx.Response)
    mock_httpx_response.status_code = 200

    return mock_httpx_response


@pytest.fixture
def mock_async_successful_httpx_response(mocker: MockerFixture) -> httpx.Response:
    async_mock_httpx_response = mocker.AsyncMock(spec=httpx.Response)
    async_mock_httpx_response.status_code = 200

    return async_mock_httpx_response


def get_studio_chat(is_async: bool = False):
    _DUMMY_MODEL = "dummy-chat-model"
    _DUMMY_MESSAGES = [
        ChatMessage(text="Hello, I need help with a signup process.", role=RoleType.USER),
        ChatMessage(
            text="Hi Alice, I can help you with that. What seems to be the problem?",
            role=RoleType.ASSISTANT,
        ),
    ]
    _DUMMY_SYSTEM = "You're a support engineer in a SaaS company"
    json_response = {
        "outputs": [
            {
                "text": "Hello, I need help with a signup process.",
                "role": "user",
                "finishReason": {"reason": "dummy_reason", "length": 1, "sequence": "1"},
            }
        ]
    }

    resource = AsyncStudioChat if is_async else StudioChat

    return (
        resource,
        {"model": _DUMMY_MODEL, "messages": _DUMMY_MESSAGES, "system": _DUMMY_SYSTEM},
        f"{_DUMMY_MODEL}/chat",
        {
            "model": _DUMMY_MODEL,
            "system": _DUMMY_SYSTEM,
            "messages": [_to_dict(message) for message in _DUMMY_MESSAGES],
            "temperature": 0.7,
            "maxTokens": 300,
            "minTokens": 0,
            "numResults": 1,
            "topP": 1.0,
            "topKReturn": 0,
        },
        httpx.Response(status_code=200, json=json_response),
        _from_dict(obj=ChatResponse, obj_dict=json_response),
    )


def get_chat_completions(is_async: bool = False):
    _DUMMY_MODEL = "dummy-chat-model"
    _DUMMY_MESSAGES = [
        ChatCompletionChatMessage(content="Hello, I need help with a signup process.", role="user"),
        ChatCompletionChatMessage(
            content="Hi Alice, I can help you with that. What seems to be the problem?",
            role="assistant",
        ),
    ]
    _EXPECTED_SERIALIZED_MESSAGES = [_to_dict(message) for message in _DUMMY_MESSAGES]
    json_response = {
        "id": "some-id",
        "choices": [
            {
                "index": 0,
                "message": {
                    "content": "Hello, I need help with a signup process.",
                    "role": "assistant",
                },
                "finish_reason": "dummy_reason",
                "logprobs": None,
            }
        ],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30,
        },
    }

    resource = AsyncChatCompletions if is_async else ChatCompletions

    return (
        resource,
        {"model": _DUMMY_MODEL, "messages": _DUMMY_MESSAGES},
        "chat/completions",
        {
            "model": _DUMMY_MODEL,
            "messages": _EXPECTED_SERIALIZED_MESSAGES,
            "stream": False,
        },
        httpx.Response(status_code=200, json=json_response),
        _from_dict(obj=ChatCompletionResponse, obj_dict=json_response),
    )


def get_studio_completion(is_async: bool = True, **kwargs):
    _DUMMY_MODEL = "dummy-completion-model"
    _DUMMY_PROMPT = "dummy-prompt"
    json_response = {
        "id": "some-id",
        "completions": [
            {
                "data": {"text": "dummy-completion", "tokens": []},
                "finishReason": {"reason": "dummy_reason", "length": 1},
            }
        ],
        "prompt": {"text": "dummy-prompt"},
    }

    resource = AsyncStudioCompletion if is_async else StudioCompletion

    return (
        resource,
        {"model": _DUMMY_MODEL, "prompt": _DUMMY_PROMPT, **kwargs},
        f"{_DUMMY_MODEL}/complete",
        {
            "model": _DUMMY_MODEL,
            "prompt": _DUMMY_PROMPT,
            **{to_lower_camel_case(k): v for k, v in kwargs.items()},
        },
        httpx.Response(status_code=200, json=json_response),
        _from_dict(obj=CompletionsResponse, obj_dict=json_response),
    )
