from ai21.models import ChatOutput, ChatResponse, FinishReason, RoleType
from ai21.models.chat import ChatCompletionResponse, ChatCompletionResponseChoice
from ai21.models.chat.chat_message import AssistantMessage
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
