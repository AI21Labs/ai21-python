from typing import Optional

import pytest

from ai21 import AI21BedrockClient, AsyncAI21BedrockClient
from ai21.clients.bedrock.bedrock_model_id import BedrockModelID
from ai21.models import Penalty
from tests.integration_tests.skip_helpers import should_skip_bedrock_integration_tests

_PROMPT = "Once upon a time, in a land far, far away, there was a"


@pytest.mark.skipif(should_skip_bedrock_integration_tests(), reason="No keys supplied for AWS. Skipping.")
@pytest.mark.parametrize(
    ids=[
        "when_no_penalties__should_return_response",
        "when_penalties__should_return_response",
    ],
    argnames=["frequency_penalty", "presence_penalty", "count_penalty"],
    argvalues=[
        (None, None, None),
        (
            Penalty(scale=0.5),
            Penalty(
                scale=0.5,
                apply_to_emojis=True,
            ),
            Penalty(
                scale=0.5,
                apply_to_emojis=True,
                apply_to_numbers=True,
                apply_to_stopwords=True,
                apply_to_punctuation=True,
                apply_to_whitespaces=True,
            ),
        ),
    ],
)
def test_completion_penalties__should_return_response(
    frequency_penalty: Optional[Penalty], presence_penalty: Optional[Penalty], count_penalty: Optional[Penalty]
):
    client = AI21BedrockClient()
    completion_args = dict(
        prompt=_PROMPT,
        max_tokens=64,
        model_id=BedrockModelID.J2_MID_V1,
        temperature=0,
        top_p=1,
        top_k_return=0,
    )

    for arg_name, penalty in [
        ("frequency_penalty", frequency_penalty),
        ("presence_penalty", presence_penalty),
        ("count_penalty", count_penalty),
    ]:
        if penalty:
            completion_args[arg_name] = penalty

    response = client.completion.create(**completion_args)

    assert response.prompt.text == _PROMPT
    assert len(response.completions) == 1

    # Check the results aren't all the same
    assert len([completion.data.text for completion in response.completions]) == 1
    for completion in response.completions:
        assert isinstance(completion.data.text, str)


@pytest.mark.skipif(should_skip_bedrock_integration_tests(), reason="No keys supplied for AWS. Skipping.")
def test_completion__when_no_model_id__should_raise_exception():
    with pytest.raises(ValueError) as e:
        client = AI21BedrockClient()
        client.completion.create(prompt=_PROMPT)

    assert e.value.args[0] == "model should be provided 'create' method call"


@pytest.mark.asyncio
@pytest.mark.skipif(should_skip_bedrock_integration_tests(), reason="No keys supplied for AWS. Skipping.")
@pytest.mark.parametrize(
    ids=[
        "when_no_penalties__should_return_response",
        "when_penalties__should_return_response",
    ],
    argnames=["frequency_penalty", "presence_penalty", "count_penalty"],
    argvalues=[
        (None, None, None),
        (
            Penalty(scale=0.5),
            Penalty(
                scale=0.5,
                apply_to_emojis=True,
            ),
            Penalty(
                scale=0.5,
                apply_to_emojis=True,
                apply_to_numbers=True,
                apply_to_stopwords=True,
                apply_to_punctuation=True,
                apply_to_whitespaces=True,
            ),
        ),
    ],
)
async def test_async_completion_penalties__should_return_response(
    frequency_penalty: Optional[Penalty], presence_penalty: Optional[Penalty], count_penalty: Optional[Penalty]
):
    client = AsyncAI21BedrockClient()
    completion_args = dict(
        prompt=_PROMPT,
        max_tokens=64,
        model_id=BedrockModelID.J2_MID_V1,
        temperature=0,
        top_p=1,
        top_k_return=0,
    )

    for arg_name, penalty in [
        ("frequency_penalty", frequency_penalty),
        ("presence_penalty", presence_penalty),
        ("count_penalty", count_penalty),
    ]:
        if penalty:
            completion_args[arg_name] = penalty

    response = await client.completion.create(**completion_args)

    assert response.prompt.text == _PROMPT
    assert len(response.completions) == 1

    # Check the results aren't all the same
    assert len([completion.data.text for completion in response.completions]) == 1
    for completion in response.completions:
        assert isinstance(completion.data.text, str)


@pytest.mark.asyncio
@pytest.mark.skipif(should_skip_bedrock_integration_tests(), reason="No keys supplied for AWS. Skipping.")
async def test_async_completion__when_no_model_id__should_raise_exception():
    with pytest.raises(ValueError) as e:
        client = AsyncAI21BedrockClient()
        await client.completion.create(prompt=_PROMPT)

    assert e.value.args[0] == "model should be provided 'create' method call"
