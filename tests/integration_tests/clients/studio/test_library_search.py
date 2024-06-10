from ai21 import AI21Client, AsyncAI21Client
import pytest


def test_library_search__when_search__should_return_relevant_results(file_in_library: str):
    client = AI21Client()
    response = client.library.search.create(
        query="What did Albert Einstein get a Nobel Prize for?", labels=["einstein"]
    )
    assert len(response.results) > 0
    for result in response.results:
        assert result.file_id == file_in_library


@pytest.mark.asyncio
async def test_async_library_search__when_search__should_return_relevant_results(file_in_library: str):
    client = AsyncAI21Client()
    response = await client.library.search.create(
        query="What did Albert Einstein get a Nobel Prize for?", labels=["einstein"]
    )
    assert len(response.results) > 0
    for result in response.results:
        assert result.file_id == file_in_library
