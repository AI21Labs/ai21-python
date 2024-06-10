import pytest
from ai21 import AI21Client, AsyncAI21Client

_CONTEXT = (
    "Holland is a geographical region[2] and former province on the western coast of"
    " the Netherlands. From the "
    "10th to the 16th century, Holland proper was a unified political region within the Holy Roman Empire as a county "
    "ruled by the counts of Holland. By the 17th century, the province of Holland had risen to become a maritime and "
    "economic power, dominating the other provinces of the newly independent Dutch Republic."
)


@pytest.mark.parametrize(
    ids=[
        "when_answer_is_in_context",
        "when_answer_not_in_context",
    ],
    argnames=["question", "is_answer_in_context", "expected_answer_type"],
    argvalues=[
        ("When did Holland become an economic power?", True, str),
        ("Is the ocean blue?", False, None),
    ],
)
def test_answer(question: str, is_answer_in_context: bool, expected_answer_type: type):
    client = AI21Client()
    response = client.answer.create(
        context=_CONTEXT,
        question=question,
    )

    assert response.answer_in_context == is_answer_in_context
    if is_answer_in_context:
        assert isinstance(response.answer, str)
    else:
        assert response.answer is None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ids=[
        "when_answer_is_in_context",
        "when_answer_not_in_context",
    ],
    argnames=["question", "is_answer_in_context", "expected_answer_type"],
    argvalues=[
        ("When did Holland become an economic power?", True, str),
        ("Is the ocean blue?", False, None),
    ],
)
async def test_async_answer(question: str, is_answer_in_context: bool, expected_answer_type: type):
    client = AsyncAI21Client()
    response = await client.answer.create(
        context=_CONTEXT,
        question=question,
    )

    assert response.answer_in_context == is_answer_in_context
    if is_answer_in_context:
        assert isinstance(response.answer, str)
    else:
        assert response.answer is None
