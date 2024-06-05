import pytest

from ai21 import AI21Client, AsyncAI21Client
from ai21.models import ChatMessage, RoleType, Penalty, FinishReason

_MODEL = "j2-ultra"
_MESSAGES = [
    ChatMessage(
        text="Hello, I need help studying for the coming test, can you teach me about the US constitution? ",
        role=RoleType.USER,
    ),
]
_SYSTEM = "You are a teacher in a public school"


def test_chat():
    num_results = 5
    messages = _MESSAGES

    client = AI21Client()
    response = client.chat.create(
        system=_SYSTEM,
        messages=messages,
        num_results=num_results,
        max_tokens=64,
        temperature=0.7,
        min_tokens=1,
        stop_sequences=["\n"],
        top_p=0.3,
        top_k_return=0,
        model=_MODEL,
        count_penalty=Penalty(
            scale=0,
            apply_to_emojis=False,
            apply_to_numbers=False,
            apply_to_stopwords=False,
            apply_to_punctuation=False,
            apply_to_whitespaces=False,
        ),
        frequency_penalty=Penalty(
            scale=0,
            apply_to_emojis=False,
            apply_to_numbers=False,
            apply_to_stopwords=False,
            apply_to_punctuation=False,
            apply_to_whitespaces=False,
        ),
        presence_penalty=Penalty(
            scale=0,
            apply_to_emojis=False,
            apply_to_numbers=False,
            apply_to_stopwords=False,
            apply_to_punctuation=False,
            apply_to_whitespaces=False,
        ),
    )

    assert response.outputs[0].role == RoleType.ASSISTANT
    assert isinstance(response.outputs[0].text, str)
    assert response.outputs[0].finish_reason == FinishReason(reason="stop", sequence="\n")

    assert len(response.outputs) == num_results


@pytest.mark.parametrize(
    ids=[
        "finish_reason_length",
        "finish_reason_endoftext",
        "finish_reason_stop_sequence",
    ],
    argnames=["max_tokens", "stop_sequences", "reason"],
    argvalues=[
        (2, "##", "length"),
        (1000, "##", "endoftext"),
        (20, ".", "stop"),
    ],
)
def test_chat_when_finish_reason_defined__should_halt_on_expected_reason(
    max_tokens: int, stop_sequences: str, reason: str
):
    client = AI21Client()
    response = client.chat.create(
        messages=_MESSAGES,
        system=_SYSTEM,
        max_tokens=max_tokens,
        model="j2-ultra",
        temperature=1,
        top_p=0,
        num_results=1,
        stop_sequences=[stop_sequences],
        top_k_return=0,
    )

    assert response.outputs[0].finish_reason.reason == reason


@pytest.mark.asyncio
async def test_async_chat():
    num_results = 5
    messages = _MESSAGES

    client = AsyncAI21Client()
    response = await client.chat.create(
        system=_SYSTEM,
        messages=messages,
        num_results=num_results,
        max_tokens=64,
        temperature=0.7,
        min_tokens=1,
        stop_sequences=["\n"],
        top_p=0.3,
        top_k_return=0,
        model=_MODEL,
        count_penalty=Penalty(
            scale=0,
            apply_to_emojis=False,
            apply_to_numbers=False,
            apply_to_stopwords=False,
            apply_to_punctuation=False,
            apply_to_whitespaces=False,
        ),
        frequency_penalty=Penalty(
            scale=0,
            apply_to_emojis=False,
            apply_to_numbers=False,
            apply_to_stopwords=False,
            apply_to_punctuation=False,
            apply_to_whitespaces=False,
        ),
        presence_penalty=Penalty(
            scale=0,
            apply_to_emojis=False,
            apply_to_numbers=False,
            apply_to_stopwords=False,
            apply_to_punctuation=False,
            apply_to_whitespaces=False,
        ),
    )

    assert response.outputs[0].role == RoleType.ASSISTANT
    assert isinstance(response.outputs[0].text, str)
    assert response.outputs[0].finish_reason == FinishReason(reason="stop", sequence="\n")

    assert len(response.outputs) == num_results


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ids=[
        "finish_reason_length",
        "finish_reason_endoftext",
        "finish_reason_stop_sequence",
    ],
    argnames=["max_tokens", "stop_sequences", "reason"],
    argvalues=[
        (2, "##", "length"),
        (1000, "##", "endoftext"),
        (20, ".", "stop"),
    ],
)
async def test_async_chat_when_finish_reason_defined__should_halt_on_expected_reason(
    max_tokens: int, stop_sequences: str, reason: str
):
    client = AsyncAI21Client()
    response = await client.chat.create(
        messages=_MESSAGES,
        system=_SYSTEM,
        max_tokens=max_tokens,
        model="j2-ultra",
        temperature=1,
        top_p=0,
        num_results=1,
        stop_sequences=[stop_sequences],
        top_k_return=0,
    )

    assert response.outputs[0].finish_reason.reason == reason
