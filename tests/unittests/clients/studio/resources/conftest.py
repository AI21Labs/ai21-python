import pytest
from pytest_mock import MockerFixture

from ai21.ai21_http_client import AI21HTTPClient
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
    ChatOutput,
    FinishReason,
    Prompt,
    Completion,
    CompletionData,
    CompletionFinishReason,
    CompletionsResponse,
    EmbedType,
    EmbedResponse,
    EmbedResult,
    GECResponse,
    Correction,
    CorrectionType,
    ImprovementType,
    ImprovementsResponse,
    Improvement,
    ParaphraseStyleType,
    ParaphraseResponse,
    Suggestion,
    DocumentType,
    SegmentationResponse,
    SummaryMethod,
    SummarizeResponse,
    SummarizeBySegmentResponse,
    SegmentSummary,
)
from ai21.models.responses.segmentation_response import Segment
from ai21.utils.typing import to_lower_camel_case


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
            "context": _DUMMY_CONTEXT,
            "question": _DUMMY_QUESTION,
        },
        AnswerResponse(id="some-id", answer_in_context=True, answer="42"),
    )


def get_studio_chat():
    _DUMMY_MODEL = "dummy-chat-model"
    _DUMMY_MESSAGES = [
        ChatMessage(content="Hello, I need help with a signup process.", role=RoleType.USER),
        ChatMessage(
            content="Hi Alice, I can help you with that. What seems to be the problem?",
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
            "messages": [{"text": message.content, "role": message.role} for message in _DUMMY_MESSAGES],
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


def get_studio_completion(**kwargs):
    _DUMMY_MODEL = "dummy-completion-model"
    _DUMMY_PROMPT = "dummy-prompt"

    return (
        StudioCompletion,
        {"model": _DUMMY_MODEL, "prompt": _DUMMY_PROMPT, **kwargs},
        f"{_DUMMY_MODEL}/complete",
        {
            "model": _DUMMY_MODEL,
            "prompt": _DUMMY_PROMPT,
            **{to_lower_camel_case(k): v for k, v in kwargs.items()},
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


def get_studio_embed():
    return (
        StudioEmbed,
        {"texts": ["text0", "text1"], "type": EmbedType.QUERY},
        "embed",
        {
            "texts": ["text0", "text1"],
            "type": EmbedType.QUERY.value,
        },
        EmbedResponse(
            id="some-id",
            results=[
                EmbedResult([1.0, 2.0, 3.0]),
                EmbedResult([4.0, 5.0, 6.0]),
            ],
        ),
    )


def get_studio_gec():
    text = "text to fi"
    return (
        StudioGEC,
        {"text": text},
        "gec",
        {
            "text": text,
        },
        GECResponse(
            id="some-id",
            corrections=[
                Correction(
                    suggestion="text to fix",
                    start_index=9,
                    end_index=10,
                    original_text=text,
                    correction_type=CorrectionType.SPELLING,
                )
            ],
        ),
    )


def get_studio_improvements():
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
        ImprovementsResponse(
            id="some-id",
            improvements=[
                Improvement(
                    suggestions=["This text is improved"],
                    start_index=0,
                    end_index=15,
                    original_text=text,
                    improvement_type=ImprovementType.FLUENCY,
                )
            ],
        ),
    )


def get_studio_paraphrase():
    text = "text to paraphrase"
    style = ParaphraseStyleType.CASUAL
    start_index = 0
    end_index = 10
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
        ParaphraseResponse(id="some-id", suggestions=[Suggestion(text="This text is paraphrased")]),
    )


def get_studio_segmentation():
    source = "segmentation text"
    source_type = DocumentType.TEXT
    return (
        StudioSegmentation,
        {"source": source, "source_type": source_type},
        "segmentation",
        {
            "source": source,
            "sourceType": source_type,
        },
        SegmentationResponse(
            id="some-id", segments=[Segment(segment_text="This text is segmented", segment_type="segment_type")]
        ),
    )


def get_studio_summarization():
    source = "text to summarize"
    source_type = "TEXT"
    focus = "text"
    summary_method = SummaryMethod.FULL_DOCUMENT
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
        SummarizeResponse(
            id="some-id",
            summary="This text is summarized",
        ),
    )


def get_studio_summarize_by_segment():
    source = "text to summarize"
    source_type = "TEXT"
    focus = "text"
    return (
        StudioSummarizeBySegment,
        {"source": source, "source_type": source_type, "focus": focus},
        "summarize-by-segment",
        {
            "source": source,
            "sourceType": source_type,
            "focus": focus,
        },
        SummarizeBySegmentResponse(
            id="some-id",
            segments=[
                SegmentSummary(
                    summary="This text is summarized",
                    segment_text="This text is segmented",
                    segment_type="segment_type",
                    segment_html=None,
                    has_summary=True,
                    highlights=[],
                )
            ],
        ),
    )
