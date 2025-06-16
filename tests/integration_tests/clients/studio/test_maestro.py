import pytest

from ai21 import AsyncAI21Client
from ai21.models.maestro import MaestroMessage


@pytest.mark.asyncio
async def test_maestro__when_upload__should_return_data_sources():  # file_in_library: str):
    client = AsyncAI21Client()
    run = await client.beta.maestro.runs.create_and_poll(
        input="When did Einstein receive a Nobel Prize?",
        tools=[{"type": "file_search"}],
        include=["data_sources"],
        poll_timeout_sec=200,
    )
    assert run.status == "completed", f"[RUN {run.id}] Expected 'completed' status"
    assert run.result, f"[RUN {run.id}] Expected a non-empty answer"
    assert run.data_sources, f"[RUN {run.id}] Expected data sources"
    assert len(run.data_sources["file_search"]) > 0, f"[RUN {run.id}] Expected at least one file search data source"
    assert run.data_sources.get("web_search") is None, f"[RUN {run.id}] Expected no web search data sources"


@pytest.mark.parametrize(
    "input_data,test_description",
    [
        ("What is the capital of France?", "string input"),
        (
            [MaestroMessage(role="user", content="What is the capital of France?")],
            "Use MaestroMessage format in a list",
        ),
        (
            [
                {"role": "user", "content": "I need help with geography."},
                {"role": "assistant", "content": "I'd be happy to help with geography questions."},
                {"role": "user", "content": "What is the capital of France?"},
            ],
            "multi-message conversation input",
        ),
    ],
)
@pytest.mark.asyncio
async def test_maestro__input_formats__should_accept_string_and_list(input_data, test_description):
    """Test that input can be passed as both string and list of dictionaries."""
    client = AsyncAI21Client()

    run = await client.beta.maestro.runs.create_and_poll(input=input_data, poll_timeout_sec=200)

    assert run.status == "completed", f"[RUN {run.id}] Expected 'completed' status for {test_description}"
    assert run.result, f"[RUN {run.id}] Expected a non-empty answer for {test_description}"
