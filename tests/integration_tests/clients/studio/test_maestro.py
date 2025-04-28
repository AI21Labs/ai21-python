import pytest

from ai21 import AsyncAI21Client


@pytest.mark.asyncio
async def test_maestro__when_upload__should_return_data_sources():  # file_in_library: str):
    client = AsyncAI21Client()
    result = await client.beta.maestro.runs.create_and_poll(
        input="When did Einstein receive a Nobel Prize?", tools=[{"type": "file_search"}], include=["data_sources"]
    )
    assert result.status == "completed", "Expected 'completed' status"
    assert result.result, "Expected a non-empty answer"
    assert result.data_sources, "Expected data sources"
    assert len(result.data_sources["file_search"]) > 0, "Expected at least one file search data source"
    assert result.data_sources.get("web_search") is None, "Expected no web search data sources"
