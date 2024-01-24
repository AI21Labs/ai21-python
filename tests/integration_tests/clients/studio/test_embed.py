from typing import List

import pytest
from ai21 import AI21Client
from ai21.models import EmbedType

_TEXT_0 = "Holland is a geographical region and former province on the western coast of the Netherlands."
_TEXT_1 = "Germany is a country in Central Europe. It is the second-most populous country in Europe after Russia"


@pytest.mark.parametrize(
    ids=[
        "when_single_text__should_return_single_embedding",
        "when_multiple_text__should_return_multiple_embeddings",
    ],
    argnames=["texts"],
    argvalues=[
        ([_TEXT_0],),
        ([_TEXT_0, _TEXT_1],),
    ],
)
def test_embed(texts: List[str]):
    client = AI21Client()
    response = client.embed.create(
        texts=texts,
        type=EmbedType.QUERY,
    )

    assert len(response.results) == len(texts)
