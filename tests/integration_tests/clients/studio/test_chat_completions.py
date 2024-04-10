import pytest

from ai21 import AI21Client
from ai21.models.chat import ChatMessage, ChatCompletionResponse
from ai21.models import RoleType


_MODEL = "jamba-instruct-preview"
_MESSAGES = [
    ChatMessage(
        content="Hello, I need help studying for the coming test, can you teach me about the US constitution? ",
        role=RoleType.USER,
    ),
]


# TODO: When the api is officially released, update the test to assert the actual response
@pytest.mark.skip(reason="API is not officially released")
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
