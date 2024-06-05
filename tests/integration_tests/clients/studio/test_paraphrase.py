import pytest

from ai21 import AI21Client, AsyncAI21Client
from ai21.models import ParaphraseStyleType


def test_paraphrase():
    client = AI21Client()
    response = client.paraphrase.create(
        text="The cat (Felis catus) is a domestic species of small carnivorous mammal",
        style=ParaphraseStyleType.FORMAL,
        start_index=0,
        end_index=20,
    )
    for suggestion in response.suggestions:
        print(suggestion.text)
    assert len(response.suggestions) > 0


def test_paraphrase__when_start_and_end_index_is_small__should_not_return_suggestions():
    client = AI21Client()
    response = client.paraphrase.create(
        text="The cat (Felis catus) is a domestic species of small carnivorous mammal",
        style=ParaphraseStyleType.GENERAL,
        start_index=0,
        end_index=5,
    )
    assert len(response.suggestions) == 0


@pytest.mark.parametrize(
    ids=["when_general", "when_casual", "when_long", "when_short", "when_formal"],
    argnames=["style"],
    argvalues=[
        (ParaphraseStyleType.GENERAL,),
        (ParaphraseStyleType.CASUAL,),
        (ParaphraseStyleType.LONG,),
        (ParaphraseStyleType.SHORT,),
        (ParaphraseStyleType.FORMAL,),
    ],
)
def test_paraphrase_styles(style: ParaphraseStyleType):
    client = AI21Client()
    response = client.paraphrase.create(
        text="Today is a beautiful day.",
        style=style,
        start_index=0,
        end_index=25,
    )

    assert len(response.suggestions) > 0


@pytest.mark.asyncio
async def test_async_paraphrase():
    client = AsyncAI21Client()
    response = await client.paraphrase.create(
        text="The cat (Felis catus) is a domestic species of small carnivorous mammal",
        style=ParaphraseStyleType.FORMAL,
        start_index=0,
        end_index=20,
    )
    for suggestion in response.suggestions:
        print(suggestion.text)
    assert len(response.suggestions) > 0


@pytest.mark.asyncio
async def test_async_paraphrase__when_start_and_end_index_is_small__should_not_return_suggestions():
    client = AsyncAI21Client()
    response = await client.paraphrase.create(
        text="The cat (Felis catus) is a domestic species of small carnivorous mammal",
        style=ParaphraseStyleType.GENERAL,
        start_index=0,
        end_index=5,
    )
    assert len(response.suggestions) == 0
