import pytest
from pytest_mock import MockerFixture

from ai21.ai21_http_client import AI21HTTPClient
from ai21.clients.studio.resources.studio_answer import StudioAnswer
from ai21.clients.studio.resources.studio_chat import StudioChat
from ai21.clients.studio.resources.studio_completion import StudioCompletion
from ai21.models import (
    AnswerResponse,
    ChatMessage,
    RoleType,
    ChatResponse,
    ChatOutput,
    FinishReason,
    Prompt,
    Completion,
    CompletionData,
    CompletionFinishReason,
    CompletionsResponse,
)


@pytest.fixture
def mock_ai21_studio_client(mocker: MockerFixture) -> AI21HTTPClient:
    return mocker.MagicMock(spec=AI21HTTPClient)


def get_studio_answer():
    _DUMMY_CONTEXT = "What is the answer to life, the universe and everything?"
    _DUMMY_QUESTION = "What is the answer?"

    return (
        StudioAnswer,
        {"context": _DUMMY_CONTEXT, "question": _DUMMY_QUESTION},
        "answer",
        {
            "answerLength": None,
            "context": _DUMMY_CONTEXT,
            "mode": None,
            "question": _DUMMY_QUESTION,
        },
        AnswerResponse(id="some-id", answer_in_context=True, answer="42"),
    )


def get_studio_chat():
    _DUMMY_MODEL = "dummy-chat-model"
    _DUMMY_MESSAGES = [
        ChatMessage(text="Hello, I need help with a signup process.", role=RoleType.USER),
        ChatMessage(
            text="Hi Alice, I can help you with that. What seems to be the problem?",
            role=RoleType.ASSISTANT,
        ),
    ]
    _DUMMY_SYSTEM = "You're a support engineer in a SaaS company"

    return (
        StudioChat,
        {"model": _DUMMY_MODEL, "messages": _DUMMY_MESSAGES, "system": _DUMMY_SYSTEM},
        f"{_DUMMY_MODEL}/chat",
        {
            "model": _DUMMY_MODEL,
            "system": _DUMMY_SYSTEM,
            "messages": [message.to_dict() for message in _DUMMY_MESSAGES],
            "temperature": 0.7,
            "maxTokens": 300,
            "minTokens": 0,
            "numResults": 1,
            "topP": 1.0,
            "topKReturn": 0,
            "stopSequences": None,
            "frequencyPenalty": None,
            "presencePenalty": None,
            "countPenalty": None,
        },
        ChatResponse(
            outputs=[
                ChatOutput(
                    text="Hello, I need help with a signup process.",
                    role="user",
                    finish_reason=FinishReason(reason="dummy_reason", length=1, sequence="1"),
                )
            ]
        ),
    )


def get_studio_completion():
    _DUMMY_MODEL = "dummy-completion-model"
    _DUMMY_PROMPT = "dummy-prompt"

    return (
        StudioCompletion,
        {"model": _DUMMY_MODEL, "prompt": _DUMMY_PROMPT},
        f"{_DUMMY_MODEL}/complete",
        {
            "model": _DUMMY_MODEL,
            "prompt": _DUMMY_PROMPT,
            "temperature": 0.7,
            "maxTokens": None,
            "minTokens": 0,
            "epoch": None,
            "numResults": 1,
            "topP": 1,
            "customModel": None,
            "topKReturn": 0,
            "stopSequences": [],
            "frequencyPenalty": None,
            "presencePenalty": None,
            "countPenalty": None,
        },
        CompletionsResponse(
            id="some-id",
            completions=[
                Completion(
                    data=CompletionData(text="dummy-completion", tokens=[]),
                    finish_reason=CompletionFinishReason(reason="dummy_reason", length=1),
                )
            ],
            prompt=Prompt(text="dummy-prompt"),
        ),
    )


def get_studio_custom_model():
    pass
