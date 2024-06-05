import pytest
from ai21 import AI21Client, AsyncAI21Client
from ai21.models import CorrectionType


@pytest.mark.parametrize(
    ids=[
        "should_fix_spelling",
        "should_fix_grammar",
        "should_fix_missing_word",
        "should_fix_punctuation",
        "should_fix_wrong_word",
    ],
    argnames=["text", "correction_type", "expected_suggestion"],
    argvalues=[
        ("jazzz is music", CorrectionType.SPELLING, "Jazz"),
        ("You am nice", CorrectionType.GRAMMAR, "are"),
        (
            "He stared out the window, lost in thought, as the raindrops against the glass.",
            CorrectionType.MISSING_WORD,
            "raindrops fell against",
        ),
        ("He is a well known author.", CorrectionType.PUNCTUATION, "well-known"),
        ("He is a dog-known author.", CorrectionType.WRONG_WORD, "well-known"),
    ],
)
def test_gec(text: str, correction_type: CorrectionType, expected_suggestion: str):
    client = AI21Client()
    response = client.gec.create(text=text)
    assert response.corrections[0].suggestion == expected_suggestion
    assert response.corrections[0].correction_type == correction_type


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ids=[
        "should_fix_spelling",
        "should_fix_grammar",
        "should_fix_missing_word",
        "should_fix_punctuation",
        "should_fix_wrong_word",
    ],
    argnames=["text", "correction_type", "expected_suggestion"],
    argvalues=[
        ("jazzz is music", CorrectionType.SPELLING, "Jazz"),
        ("You am nice", CorrectionType.GRAMMAR, "are"),
        (
            "He stared out the window, lost in thought, as the raindrops against the glass.",
            CorrectionType.MISSING_WORD,
            "raindrops fell against",
        ),
        ("He is a well known author.", CorrectionType.PUNCTUATION, "well-known"),
        ("He is a dog-known author.", CorrectionType.WRONG_WORD, "well-known"),
    ],
)
async def test_async_gec(text: str, correction_type: CorrectionType, expected_suggestion: str):
    client = AsyncAI21Client()
    response = await client.gec.create(text=text)
    assert response.corrections[0].suggestion == expected_suggestion
    assert response.corrections[0].correction_type == correction_type
