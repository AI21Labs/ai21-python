from ai21 import AI21Client
from ai21.models.chat import ChatMessage, ChatCompletionResponse, ChatCompletionChunk, ChoicesChunk, ChoiceDelta
from ai21.models import RoleType

_MODEL = "jamba-instruct-preview"
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
    assert response.choices[0].message.content
    assert response.choices[0].message.role


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
