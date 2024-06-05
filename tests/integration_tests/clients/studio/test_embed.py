from typing import List

import pytest
from ai21 import AI21Client, AsyncAI21Client
from ai21.models import EmbedType

_TEXT_0 = "Holland is a geographical region and former province on the western coast of the Netherlands."
_TEXT_1 = "Germany is a country in Central Europe. It is the second-most populous country in Europe after Russia"

_SEGMENT_0 = "The sun sets behind the mountains,"
_SEGMENT_1 = "casting a warm glow over"
_SEGMENT_2 = "the city of Amsterdam."


@pytest.mark.parametrize(
    ids=[
        "when_single_text_and_query__should_return_single_embedding",
        "when_multiple_text_and_query__should_return_multiple_embeddings",
        "when_single_text_and_segment__should_return_single_embedding",
        "when_multiple_text_and_segment__should_return_multiple_embeddings",
    ],
    argnames=["texts", "type"],
    argvalues=[
        ([_TEXT_0], EmbedType.QUERY),
        ([_TEXT_0, _TEXT_1], EmbedType.QUERY),
        ([_SEGMENT_0], EmbedType.SEGMENT),
        ([_SEGMENT_0, _SEGMENT_1, _SEGMENT_2], EmbedType.SEGMENT),
    ],
)
def test_embed(texts: List[str], type: EmbedType):
    client = AI21Client()
    response = client.embed.create(
        texts=texts,
        type=type,
    )

    assert len(response.results) == len(texts)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ids=[
        "when_single_text_and_query__should_return_single_embedding",
        "when_multiple_text_and_query__should_return_multiple_embeddings",
        "when_single_text_and_segment__should_return_single_embedding",
        "when_multiple_text_and_segment__should_return_multiple_embeddings",
    ],
    argnames=["texts", "type"],
    argvalues=[
        ([_TEXT_0], EmbedType.QUERY),
        ([_TEXT_0, _TEXT_1], EmbedType.QUERY),
        ([_SEGMENT_0], EmbedType.SEGMENT),
        ([_SEGMENT_0, _SEGMENT_1, _SEGMENT_2], EmbedType.SEGMENT),
    ],
)
async def test_async_embed(texts: List[str], type: EmbedType):
    client = AsyncAI21Client()
    response = await client.embed.create(
        texts=texts,
        type=type,
    )

    assert len(response.results) == len(texts)
