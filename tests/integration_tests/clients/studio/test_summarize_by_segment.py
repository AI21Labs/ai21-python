import pytest

from ai21 import AI21Client, AsyncAI21Client
from ai21.errors import UnprocessableEntity
from ai21.models import DocumentType

_SOURCE_TEXT = """Holland is a geographical region and former province on the western coast of the Netherlands.
 From the 10th to the 16th century, Holland proper was  a unified political
 region within the Holy Roman Empire as a county ruled by the counts of Holland.
  By the 17th century, the province of Holland had risen to become a maritime and economic power,
   dominating the other provinces of the newly independent Dutch Republic."""

_SOURCE_URL = "https://en.wikipedia.org/wiki/Holland"


def test_summarize_by_segment__when_text__should_return_response():
    client = AI21Client()
    response = client.summarize_by_segment.create(
        source=_SOURCE_TEXT,
        source_type=DocumentType.TEXT,
        focus="Holland",
    )
    assert isinstance(response.segments[0].segment_text, str)
    assert response.segments[0].segment_html is None
    assert isinstance(response.segments[0].summary, str)
    assert len(response.segments[0].highlights) > 0
    assert response.segments[0].segment_type == "normal_text"
    assert response.segments[0].has_summary


def test_summarize_by_segment__when_url__should_return_response():
    client = AI21Client()
    response = client.summarize_by_segment.create(
        source=_SOURCE_URL,
        source_type=DocumentType.URL,
        focus="Holland",
    )
    assert isinstance(response.segments[0].segment_text, str)
    assert isinstance(response.segments[0].segment_html, str)
    assert isinstance(response.segments[0].summary, str)
    assert response.segments[0].segment_type == "normal_text"
    assert len(response.segments[0].highlights) > 0
    assert response.segments[0].has_summary


@pytest.mark.parametrize(
    ids=[
        "when_source_is_text_and_source_type_is_url__should_raise_error",
        "when_source_is_url_and_source_type_is_text__should_raise_error",
    ],
    argnames=["source", "source_type"],
    argvalues=[
        (_SOURCE_TEXT, DocumentType.URL),
        (_SOURCE_URL, DocumentType.TEXT),
    ],
)
def test_summarize_by_segment__source_and_source_type_misalignment(source: str, source_type: DocumentType):
    focus = "Holland"

    client = AI21Client()
    with pytest.raises(UnprocessableEntity):
        client.summarize_by_segment.create(
            source=source,
            source_type=source_type,
            focus=focus,
        )


@pytest.mark.asyncio
async def test_async_summarize_by_segment__when_text__should_return_response():
    client = AsyncAI21Client()
    response = await client.summarize_by_segment.create(
        source=_SOURCE_TEXT,
        source_type=DocumentType.TEXT,
        focus="Holland",
    )
    assert isinstance(response.segments[0].segment_text, str)
    assert response.segments[0].segment_html is None
    assert isinstance(response.segments[0].summary, str)
    assert len(response.segments[0].highlights) > 0
    assert response.segments[0].segment_type == "normal_text"
    assert response.segments[0].has_summary


@pytest.mark.asyncio
async def test_async_summarize_by_segment__when_url__should_return_response():
    client = AsyncAI21Client()
    response = await client.summarize_by_segment.create(
        source=_SOURCE_URL,
        source_type=DocumentType.URL,
        focus="Holland",
    )
    assert isinstance(response.segments[0].segment_text, str)
    assert isinstance(response.segments[0].segment_html, str)
    assert isinstance(response.segments[0].summary, str)
    assert response.segments[0].segment_type == "normal_text"
    assert len(response.segments[0].highlights) > 0
    assert response.segments[0].has_summary


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ids=[
        "when_source_is_text_and_source_type_is_url__should_raise_error",
        "when_source_is_url_and_source_type_is_text__should_raise_error",
    ],
    argnames=["source", "source_type"],
    argvalues=[
        (_SOURCE_TEXT, DocumentType.URL),
        (_SOURCE_URL, DocumentType.TEXT),
    ],
)
async def test_async_summarize_by_segment__source_and_source_type_misalignment(source: str, source_type: DocumentType):
    focus = "Holland"

    client = AsyncAI21Client()
    with pytest.raises(UnprocessableEntity):
        await client.summarize_by_segment.create(
            source=source,
            source_type=source_type,
            focus=focus,
        )
