from ai21 import AI21Client
from ai21.models.chat import ChatMessage
from ai21.models import RoleType
from ai21.models.chat.chat_completion_response import ChatCompletionResponse


_MODEL = "jamba-instruct"
_MESSAGES = [
    ChatMessage(
        content="Hello, I need help studying for the coming test, can you teach me about the US constitution? ",
        role=RoleType.USER,
    ),
]


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
    assert response.choices[0]
