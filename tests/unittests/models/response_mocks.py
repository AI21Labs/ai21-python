from ai21.models import (
    ChatResponse,
    ChatOutput,
    RoleType,
    FinishReason,
    CompletionsResponse,
    Prompt,
    Completion,
    CompletionFinishReason,
    CompletionData,
    SegmentationResponse,
    SummarizeResponse,
    SummarizeBySegmentResponse,
    SegmentSummary,
    Highlight,
)
from ai21.models.chat import ChatCompletionResponse, ChatCompletionResponseChoice
from ai21.models.chat.chat_message import AssistantMessage
from ai21.models.responses.segmentation_response import Segment
from ai21.models.usage_info import UsageInfo


def get_chat_response():
    expected_dict = {
        "outputs": [
            {
                "text": "It's a big question, and the answer is different for everyone. Some people",
                "role": "assistant",
                "finishReason": {"reason": "length", "length": 10, "sequence": None},
            },
        ],
    }

    output = ChatOutput(
        text="It's a big question, and the answer is different for everyone. Some people",
        role=RoleType.ASSISTANT,
        finish_reason=FinishReason(reason="length", length=10),
    )
    chat_response = ChatResponse(outputs=[output])

    return chat_response, expected_dict, ChatResponse


def get_chat_completions_response():
    expected_dict = {
        "id": "123",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "I apologize for any inconvenience you're experiencing. Can you please provide me with "
                    "more information about the issue you're facing? For example, are you receiving an "
                    "error message when you try to sign up with your Google account? If so, what does the "
                    "error message say?",
                    "tool_calls": None,
                },
                "logprobs": None,
                "finish_reason": "stop",
            }
        ],
        "usage": {"prompt_tokens": 105, "completion_tokens": 61, "total_tokens": 166},
    }

    choice = ChatCompletionResponseChoice(
        index=0,
        message=AssistantMessage(
            role="assistant",
            content="I apologize for any inconvenience you're experiencing. Can you please provide me with more "
            "information about the issue you're facing? For example, are you receiving an error message when "
            "you try to sign up with your Google account? If so, what does the error message say?",
        ),
        finish_reason="stop",
    )

    chat_completions_response = ChatCompletionResponse(
        id="123",
        choices=[choice],
        usage=UsageInfo(prompt_tokens=105, completion_tokens=61, total_tokens=166),
    )

    return chat_completions_response, expected_dict, ChatCompletionResponse


def get_completions_response():
    expected_dict = {
        "id": "123-abc",
        "prompt": {
            "text": "life is like ",
            "tokens": [
                {
                    "generatedToken": {
                        "token": "▁life▁is",
                        "logprob": -14.273218154907227,
                        "raw_logprob": -14.273218154907227,
                    },
                    "topTokens": None,
                    "textRange": {"start": 0, "end": 7},
                },
            ],
        },
        "completions": [
            {
                "data": {
                    "text": "\nlife is like a journey, full of ups and downs, twists and turns. It is unpredictable "
                    "and can be challenging, but it is also",
                    "tokens": [
                        {
                            "generatedToken": {
                                "token": "<|newline|>",
                                "logprob": -0.006884856149554253,
                                "raw_logprob": -0.12210073322057724,
                            },
                            "topTokens": None,
                            "textRange": {"start": 0, "end": 1},
                        },
                    ],
                },
                "finishReason": {"reason": "length", "length": 16},
            }
        ],
    }

    prompt = Prompt(
        text="life is like ",
        tokens=[
            {
                "generatedToken": {
                    "token": "▁life▁is",
                    "logprob": -14.273218154907227,
                    "raw_logprob": -14.273218154907227,
                },
                "topTokens": None,
                "textRange": {"start": 0, "end": 7},
            },
        ],
    )
    completion = Completion(
        data=CompletionData(
            text="\nlife is like a journey, full of ups and downs, twists and turns. It is unpredictable and can be "
            "challenging, but it is also",
            tokens=[
                {
                    "generatedToken": {
                        "token": "<|newline|>",
                        "logprob": -0.006884856149554253,
                        "raw_logprob": -0.12210073322057724,
                    },
                    "topTokens": None,
                    "textRange": {"start": 0, "end": 1},
                }
            ],
        ),
        finish_reason=CompletionFinishReason(reason="length", length=16),
    )
    completion_response = CompletionsResponse(id="123-abc", prompt=prompt, completions=[completion])

    return completion_response, expected_dict, CompletionsResponse


def get_segmentation_response():
    expected_dict = {
        "id": "123",
        "segments": [
            {"segmentText": "Further reading", "segmentType": "h2"},
        ],
    }

    segmentation_response = SegmentationResponse(
        id="123", segments=[Segment(segment_text="Further reading", segment_type="h2")]
    )

    return segmentation_response, expected_dict, SegmentationResponse


def get_summarize_response():
    expected_dict = {
        "id": "123",
        "summary": "The blue whale is a marine mammal that lives off California's coast.",
    }

    summarization_response = SummarizeResponse(
        id="123",
        summary="The blue whale is a marine mammal that lives off California's coast.",
    )

    return summarization_response, expected_dict, SummarizeResponse


def get_summarize_by_segment_response():
    expected_dict = {
        "id": "123",
        "segments": [
            {
                "summary": "The blue whale is the largest animal known ever to have existed.",
                "segmentType": "normal_text",
                "hasSummary": True,
                "highlights": [{"text": "The blue whale", "startIndex": 0, "endIndex": 14}],
                "segmentHtml": None,
                "segmentText": None,
            },
        ],
    }

    summarization_response = SummarizeBySegmentResponse(
        id="123",
        segments=[
            SegmentSummary(
                summary="The blue whale is the largest animal known ever to have existed.",
                segment_type="normal_text",
                has_summary=True,
                highlights=[Highlight(text="The blue whale", start_index=0, end_index=14)],
            ),
        ],
    )

    return summarization_response, expected_dict, SummarizeBySegmentResponse
