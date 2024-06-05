import pytest
from ai21 import AI21Client, AsyncAI21Client
from ai21.errors import UnprocessableEntity
from ai21.models import DocumentType

_SOURCE_TEXT = """Holland is a geographical region and former province on the western coast of the
Netherlands. From the 10th to the 16th century, Holland proper was  a unified political
 region within the Holy Roman Empire as a county ruled by the counts of Holland.
  By the 17th century, the province of Holland had risen to become a maritime and economic power,
   dominating the other provinces of the newly independent Dutch Republic."""

_SOURCE_URL = "https://en.wikipedia.org/wiki/Holland"


@pytest.mark.parametrize(
    ids=[
        "when_source_is_text__should_return_a_segments",
        "when_source_is_url__should_return_a_segments",
    ],
    argnames=["source", "source_type"],
    argvalues=[
        (_SOURCE_TEXT, DocumentType.TEXT),
        (_SOURCE_URL, DocumentType.URL),
    ],
)
def test_segmentation(source: str, source_type: DocumentType):
    client = AI21Client()

    response = client.segmentation.create(
        source=source,
        source_type=source_type,
    )

    assert isinstance(response.segments[0].segment_text, str)
    assert response.segments[0].segment_type is not None


@pytest.mark.parametrize(
    ids=[
        "when_source_is_text_and_source_type_is_url__should_raise_error",
        # "when_source_is_url_and_source_type_is_text__should_raise_error",
    ],
    argnames=["source", "source_type"],
    argvalues=[
        (_SOURCE_TEXT, DocumentType.URL),
        # (_SOURCE_URL, DocumentType.TEXT),
    ],
)
def test_segmentation__source_and_source_type_misalignment(source: str, source_type: DocumentType):
    client = AI21Client()
    with pytest.raises(UnprocessableEntity):
        client.segmentation.create(
            source=source,
            source_type=source_type,
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ids=[
        "when_source_is_text__should_return_a_segments",
        "when_source_is_url__should_return_a_segments",
    ],
    argnames=["source", "source_type"],
    argvalues=[
        (_SOURCE_TEXT, DocumentType.TEXT),
        (_SOURCE_URL, DocumentType.URL),
    ],
)
async def test_async_segmentation(source: str, source_type: DocumentType):
    client = AsyncAI21Client()

    response = await client.segmentation.create(
        source=source,
        source_type=source_type,
    )

    assert isinstance(response.segments[0].segment_text, str)
    assert response.segments[0].segment_type is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ids=[
        "when_source_is_text_and_source_type_is_url__should_raise_error",
        # "when_source_is_url_and_source_type_is_text__should_raise_error",
    ],
    argnames=["source", "source_type"],
    argvalues=[
        (_SOURCE_TEXT, DocumentType.URL),
        # (_SOURCE_URL, DocumentType.TEXT),
    ],
)
async def test_async_segmentation__source_and_source_type_misalignment(source: str, source_type: DocumentType):
    client = AsyncAI21Client()
    with pytest.raises(UnprocessableEntity):
        await client.segmentation.create(
            source=source,
            source_type=source_type,
        )
