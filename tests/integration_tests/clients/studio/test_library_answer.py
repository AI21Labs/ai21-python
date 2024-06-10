import pytest
from ai21 import AI21Client, AsyncAI21Client


def test_library_answer__when_answer_not_in_context__should_return_false(file_in_library: str):
    client = AI21Client()
    response = client.library.answer.create(question="Who is Tony Stark?")
    assert response.answer is None
    assert not response.answer_in_context


def test_library_answer__when_answer_in_context__should_return_true(file_in_library: str):
    client = AI21Client()
    response = client.library.answer.create(question="Who was Albert Einstein?")
    assert response.answer is not None
    assert response.answer_in_context
    assert response.sources[0].file_id == file_in_library


@pytest.mark.asyncio
async def test_async_library_answer__when_answer_not_in_context__should_return_false(file_in_library: str):
    client = AsyncAI21Client()
    response = await client.library.answer.create(question="Who is Tony Stark?")
    assert response.answer is None
    assert not response.answer_in_context


@pytest.mark.asyncio
async def test_async_library_answer__when_answer_in_context__should_return_true(file_in_library: str):
    client = AsyncAI21Client()
    response = await client.library.answer.create(question="Who was Albert Einstein?")
    assert response.answer is not None
    assert response.answer_in_context
    assert response.sources[0].file_id == file_in_library
