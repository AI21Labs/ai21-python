import pytest

from typing import Dict
from ai21 import AI21Client, AsyncAI21Client
from ai21.models import Penalty

_PROMPT = """
User: Haven't received a confirmation email for my order #12345.
Assistant: I'm sorry to hear that. I'll look into it right away.
User: Can you please let me know when I can expect to receive it?
"""


def test_completion():
    num_results = 3

    client = AI21Client()
    response = client.completion.create(
        prompt=_PROMPT,
        max_tokens=64,
        model="j2-ultra",
        temperature=0.7,
        top_p=0.2,
        top_k_return=0.2,
        stop_sequences=["##"],
        num_results=num_results,
        custom_model=None,
        epoch=1,
        logit_bias={"▁a▁box▁of": -100.0},
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

    assert response.prompt.text == _PROMPT
    assert len(response.completions) == num_results
    # Check the results aren't all the same
    assert len([completion.data.text for completion in response.completions]) == num_results
    for completion in response.completions:
        assert isinstance(completion.data.text, str)


def test_completion_when_temperature_1_and_top_p_is_0__should_return_same_response():
    num_results = 5

    client = AI21Client()
    response = client.completion.create(
        prompt=_PROMPT,
        max_tokens=64,
        model="j2-ultra",
        temperature=1,
        top_p=0,
        top_k_return=0,
        num_results=num_results,
        epoch=1,
    )

    assert response.prompt.text == _PROMPT
    assert len(response.completions) == num_results
    # Verify all results are the same
    assert len(set([completion.data.text for completion in response.completions])) == 1


@pytest.mark.parametrize(
    ids=[
        "finish_reason_length",
        "finish_reason_endoftext",
        "finish_reason_stop_sequence",
    ],
    argnames=["max_tokens", "stop_sequences", "reason"],
    argvalues=[
        (10, "##", "length"),
        (100, "##", "endoftext"),
        (50, "\n", "stop"),
    ],
)
def test_completion_when_finish_reason_defined__should_halt_on_expected_reason(
    max_tokens: int, stop_sequences: str, reason: str
):
    client = AI21Client()
    response = client.completion.create(
        prompt=_PROMPT,
        max_tokens=max_tokens,
        model="j2-ultra",
        temperature=1,
        top_p=0,
        num_results=1,
        stop_sequences=[stop_sequences],
        top_k_return=0,
        epoch=1,
    )

    assert response.completions[0].finish_reason.reason == reason


@pytest.mark.parametrize(
    ids=[
        "no_logit_bias",
        "logit_bias_negative",
    ],
    argnames=["expected_result", "logit_bias"],
    argvalues=[(" a box of chocolates", None), (" riding a bicycle", {"▁a▁box▁of": -100.0})],
)
def test_completion_logit_bias__should_impact_on_response(expected_result: str, logit_bias: Dict[str, float]):
    client = AI21Client()
    response = client.completion.create(
        prompt="Life is like",
        max_tokens=3,
        model="j2-ultra",
        temperature=0,
        logit_bias=logit_bias,
    )

    assert response.completions[0].data.text.strip() == expected_result.strip()


@pytest.mark.asyncio
async def test_async_completion():
    num_results = 3

    client = AsyncAI21Client()
    response = await client.completion.create(
        prompt=_PROMPT,
        max_tokens=64,
        model="j2-ultra",
        temperature=0.7,
        top_p=0.2,
        top_k_return=0.2,
        stop_sequences=["##"],
        num_results=num_results,
        custom_model=None,
        epoch=1,
        logit_bias={"▁a▁box▁of": -100.0},
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

    assert response.prompt.text == _PROMPT
    assert len(response.completions) == num_results
    # Check the results aren't all the same
    assert len([completion.data.text for completion in response.completions]) == num_results
    for completion in response.completions:
        assert isinstance(completion.data.text, str)


@pytest.mark.asyncio
async def test_async_completion_when_temperature_1_and_top_p_is_0__should_return_same_response():
    num_results = 5

    client = AsyncAI21Client()
    response = await client.completion.create(
        prompt=_PROMPT,
        max_tokens=64,
        model="j2-ultra",
        temperature=1,
        top_p=0,
        top_k_return=0,
        num_results=num_results,
        epoch=1,
    )

    assert response.prompt.text == _PROMPT
    assert len(response.completions) == num_results
    # Verify all results are the same
    assert len(set([completion.data.text for completion in response.completions])) == 1


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ids=[
        "finish_reason_length",
        "finish_reason_endoftext",
        "finish_reason_stop_sequence",
    ],
    argnames=["max_tokens", "stop_sequences", "reason"],
    argvalues=[
        (10, "##", "length"),
        (100, "##", "endoftext"),
        (50, "\n", "stop"),
    ],
)
async def test_async_completion_when_finish_reason_defined__should_halt_on_expected_reason(
    max_tokens: int, stop_sequences: str, reason: str
):
    client = AsyncAI21Client()
    response = await client.completion.create(
        prompt=_PROMPT,
        max_tokens=max_tokens,
        model="j2-ultra",
        temperature=1,
        top_p=0,
        num_results=1,
        stop_sequences=[stop_sequences],
        top_k_return=0,
        epoch=1,
    )

    assert response.completions[0].finish_reason.reason == reason


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ids=[
        "no_logit_bias",
        "logit_bias_negative",
    ],
    argnames=["expected_result", "logit_bias"],
    argvalues=[(" a box of chocolates", None), (" riding a bicycle", {"▁a▁box▁of": -100.0})],
)
async def test_async_completion_logit_bias__should_impact_on_response(
    expected_result: str, logit_bias: Dict[str, float]
):
    client = AsyncAI21Client()
    response = await client.completion.create(
        prompt="Life is like",
        max_tokens=3,
        model="j2-ultra",
        temperature=0,
        logit_bias=logit_bias,
    )

    assert response.completions[0].data.text.strip() == expected_result.strip()
