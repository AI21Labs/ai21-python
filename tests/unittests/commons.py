FAKE_CHAT_COMPLETION_RESPONSE_DICT = {
    "id": "cmpl-392a6a33e5204aa7a2070be4d0ddbc0a",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Test",
            },
            "logprobs": None,
            "finishReason": "stop",
        }
    ],
    "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2},
}

FAKE_AUTH_HEADERS = {"Authorization": "Bearer fake-token"}
