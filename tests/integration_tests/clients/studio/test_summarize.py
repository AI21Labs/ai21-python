import pytest

from ai21 import AI21Client, AsyncAI21Client
from ai21.errors import UnprocessableEntity
from ai21.models import DocumentType, SummaryMethod

_SOURCE_TEXT = """Holland is a geographical region and former province on the western coast of the
Netherlands. From the 10th to the 16th century, Holland proper was  a unified political
 region within the Holy Roman Empire as a county ruled by the counts of Holland.
  By the 17th century, the province of Holland had risen to become a maritime and economic power,
   dominating the other provinces of the newly independent Dutch Republic."""

_SOURCE_URL = "https://en.wikipedia.org/wiki/Holland"


@pytest.mark.parametrize(
    ids=[
        "when_source_is_text__should_return_a_suggestion",
        "when_source_is_url__should_return_a_suggestion",
    ],
    argnames=["source", "source_type"],
    argvalues=[
        (_SOURCE_TEXT, DocumentType.TEXT),
        (_SOURCE_URL, DocumentType.URL),
    ],
)
def test_summarize(source: str, source_type: DocumentType):
    focus = "Holland"

    client = AI21Client()
    response = client.summarize.create(
        source=source,
        source_type=source_type,
        summary_method=SummaryMethod.SEGMENTS,
        focus=focus,
    )
    assert response.summary is not None
    assert focus in response.summary


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
def test_summarize__source_and_source_type_misalignment(source: str, source_type: DocumentType):
    focus = "Holland"

    client = AI21Client()
    with pytest.raises(UnprocessableEntity):
        client.summarize.create(
            source=source,
            source_type=source_type,
            summary_method=SummaryMethod.SEGMENTS,
            focus=focus,
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ids=[
        "when_source_is_text__should_return_a_suggestion",
        "when_source_is_url__should_return_a_suggestion",
    ],
    argnames=["source", "source_type"],
    argvalues=[
        (_SOURCE_TEXT, DocumentType.TEXT),
        (_SOURCE_URL, DocumentType.URL),
    ],
)
async def test_async_summarize(source: str, source_type: DocumentType):
    focus = "Holland"

    client = AsyncAI21Client()
    response = await client.summarize.create(
        source=source,
        source_type=source_type,
        summary_method=SummaryMethod.SEGMENTS,
        focus=focus,
    )
    assert response.summary is not None
    assert focus in response.summary


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
async def test_async_summarize__source_and_source_type_misalignment(source: str, source_type: DocumentType):
    focus = "Holland"

    client = AsyncAI21Client()
    with pytest.raises(UnprocessableEntity):
        await client.summarize.create(
            source=source,
            source_type=source_type,
            summary_method=SummaryMethod.SEGMENTS,
            focus=focus,
        )
