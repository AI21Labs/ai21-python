import pytest
import httpx
from pytest_mock import MockerFixture

from ai21.ai21_http_client import AI21HTTPClient
from ai21.clients.studio.resources.chat import ChatCompletions
from ai21.clients.studio.resources.studio_answer import StudioAnswer
from ai21.clients.studio.resources.studio_chat import StudioChat
from ai21.clients.studio.resources.studio_completion import StudioCompletion
from ai21.clients.studio.resources.studio_embed import StudioEmbed
from ai21.clients.studio.resources.studio_gec import StudioGEC
from ai21.clients.studio.resources.studio_improvements import StudioImprovements
from ai21.clients.studio.resources.studio_paraphrase import StudioParaphrase
from ai21.clients.studio.resources.studio_segmentation import StudioSegmentation
from ai21.clients.studio.resources.studio_summarize import StudioSummarize
from ai21.clients.studio.resources.studio_summarize_by_segment import StudioSummarizeBySegment
from ai21.models import (
    AnswerResponse,
    ChatMessage,
    RoleType,
    ChatResponse,
    CompletionsResponse,
    EmbedType,
    EmbedResponse,
    GECResponse,
    ImprovementType,
    ImprovementsResponse,
    ParaphraseStyleType,
    ParaphraseResponse,
    DocumentType,
    SegmentationResponse,
    SummaryMethod,
    SummarizeResponse,
    SummarizeBySegmentResponse,
)
from ai21.models.chat import (
    ChatMessage as ChatCompletionChatMessage,
    ChatCompletionResponse,
)
from ai21.utils.typing import to_lower_camel_case


@pytest.fixture
def mock_ai21_studio_client(mocker: MockerFixture) -> AI21HTTPClient:
    return mocker.MagicMock(spec=AI21HTTPClient)


@pytest.fixture
def mock_successful_httpx_response(mocker: MockerFixture) -> httpx.Response:
    mock_httpx_response = mocker.Mock(spec=httpx.Response)
    mock_httpx_response.status_code = 200

    return mock_httpx_response


def get_studio_answer():
    _DUMMY_CONTEXT = "What is the answer to life, the universe and everything?"
    _DUMMY_QUESTION = "What is the answer?"
    json_response = {"id": "some-id", "answer_in_context": True, "answer": "42"}

    return (
        StudioAnswer,
        {"context": _DUMMY_CONTEXT, "question": _DUMMY_QUESTION},
        "answer",
        {
            "context": _DUMMY_CONTEXT,
            "question": _DUMMY_QUESTION,
        },
        httpx.Response(status_code=200, json=json_response),
        AnswerResponse.from_dict(json_response),
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
    json_response = {
        "outputs": [
            {
                "text": "Hello, I need help with a signup process.",
                "role": "user",
                "finishReason": {"reason": "dummy_reason", "length": 1, "sequence": "1"},
            }
        ]
    }

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
        httpx.Response(status_code=200, json=json_response),
        ChatResponse.from_dict(json_response),
    )


def get_chat_completions():
    _DUMMY_MODEL = "dummy-chat-model"
    _DUMMY_MESSAGES = [
        ChatCompletionChatMessage(content="Hello, I need help with a signup process.", role="user"),
        ChatCompletionChatMessage(
            content="Hi Alice, I can help you with that. What seems to be the problem?",
            role="assistant",
        ),
    ]
    _EXPECTED_SERIALIZED_MESSAGES = [message.to_dict() for message in _DUMMY_MESSAGES]
    json_response = {
        "id": "some-id",
        "choices": [
            {
                "index": 0,
                "message": {
                    "content": "Hello, I need help with a signup process.",
                    "role": "user",
                },
                "finishReason": "dummy_reason",
                "logprobs": None,
            }
        ],
        "usage": {
            "promptTokens": 10,
            "completionTokens": 20,
            "totalTokens": 30,
        },
    }

    return (
        ChatCompletions,
        {"model": _DUMMY_MODEL, "messages": _DUMMY_MESSAGES},
        "chat/completions",
        {
            "model": _DUMMY_MODEL,
            "messages": _EXPECTED_SERIALIZED_MESSAGES,
            "stream": False,
        },
        httpx.Response(status_code=200, json=json_response),
        ChatCompletionResponse.from_dict(json_response),
    )


def get_studio_completion(**kwargs):
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

    return (
        StudioCompletion,
        {"model": _DUMMY_MODEL, "prompt": _DUMMY_PROMPT, **kwargs},
        f"{_DUMMY_MODEL}/complete",
        {
            "model": _DUMMY_MODEL,
            "prompt": _DUMMY_PROMPT,
            **{to_lower_camel_case(k): v for k, v in kwargs.items()},
        },
        httpx.Response(status_code=200, json=json_response),
        CompletionsResponse.from_dict(json_response),
    )


def get_studio_embed():
    json_response = {
        "id": "some-id",
        "results": [
            {"embedding": [1.0, 2.0, 3.0]},
            {"embedding": [4.0, 5.0, 6.0]},
        ],
    }

    return (
        StudioEmbed,
        {"texts": ["text0", "text1"], "type": EmbedType.QUERY},
        "embed",
        {
            "texts": ["text0", "text1"],
            "type": EmbedType.QUERY.value,
        },
        httpx.Response(status_code=200, json=json_response),
        EmbedResponse.from_dict(json_response),
    )


def get_studio_gec():
    json_response = {
        "id": "some-id",
        "corrections": [
            {
                "suggestion": "text to fix",
                "startIndex": 9,
                "endIndex": 10,
                "originalText": "text to fi",
                "correctionType": "Spelling",
            }
        ],
    }
    text = "text to fi"

    return (
        StudioGEC,
        {"text": text},
        "gec",
        {
            "text": text,
        },
        httpx.Response(status_code=200, json=json_response),
        GECResponse.from_dict(json_response),
    )


def get_studio_improvements():
    json_response = {
        "id": "some-id",
        "improvements": [
            {
                "suggestions": ["This text is improved"],
                "startIndex": 0,
                "endIndex": 15,
                "originalText": "text to improve",
                "improvementType": "FLUENCY",
            }
        ],
    }
    text = "text to improve"
    types = [ImprovementType.FLUENCY]

    return (
        StudioImprovements,
        {"text": text, "types": types},
        "improvements",
        {
            "text": text,
            "types": types,
        },
        httpx.Response(status_code=200, json=json_response),
        ImprovementsResponse.from_dict(json_response),
    )


def get_studio_paraphrase():
    text = "text to paraphrase"
    style = ParaphraseStyleType.CASUAL
    start_index = 0
    end_index = 10
    json_response = {
        "id": "some-id",
        "suggestions": [
            {
                "text": "This text is paraphrased",
            }
        ],
    }

    return (
        StudioParaphrase,
        {"text": text, "style": style, "start_index": start_index, "end_index": end_index},
        "paraphrase",
        {
            "text": text,
            "style": style,
            "startIndex": start_index,
            "endIndex": end_index,
        },
        httpx.Response(status_code=200, json=json_response),
        ParaphraseResponse.from_dict(json_response),
    )


def get_studio_segmentation():
    source = "segmentation text"
    source_type = DocumentType.TEXT
    json_response = {
        "id": "some-id",
        "segments": [
            {
                "segmentText": "This text is segmented",
                "segmentType": "segment_type",
            }
        ],
    }

    return (
        StudioSegmentation,
        {"source": source, "source_type": source_type},
        "segmentation",
        {
            "source": source,
            "sourceType": source_type,
        },
        httpx.Response(status_code=200, json=json_response),
        SegmentationResponse.from_dict(json_response),
    )


def get_studio_summarization():
    source = "text to summarize"
    source_type = "TEXT"
    focus = "text"
    summary_method = SummaryMethod.FULL_DOCUMENT
    json_response = {
        "id": "some-id",
        "summary": "This text is summarized",
    }

    return (
        StudioSummarize,
        {"source": source, "source_type": source_type, "focus": focus, "summary_method": summary_method},
        "summarize",
        {
            "source": source,
            "sourceType": source_type,
            "focus": focus,
            "summaryMethod": summary_method,
        },
        httpx.Response(status_code=200, json=json_response),
        SummarizeResponse.from_dict(json_response),
    )


def get_studio_summarize_by_segment():
    source = "text to summarize"
    source_type = "TEXT"
    focus = "text"
    json_response = {
        "id": "some-id",
        "segments": [
            {
                "summary": "This text is summarized",
                "segmentText": "This text is segmented",
                "segmentHtml": "",
                "segmentType": "segment_type",
                "hasSummary": True,
                "highlights": [],
            }
        ],
    }

    return (
        StudioSummarizeBySegment,
        {"source": source, "source_type": source_type, "focus": focus},
        "summarize-by-segment",
        {
            "source": source,
            "sourceType": source_type,
            "focus": focus,
        },
        httpx.Response(status_code=200, json=json_response),
        SummarizeBySegmentResponse.from_dict(json_response),
    )
