from typing import List

import pytest
from ai21.tokenizers.factory import get_async_tokenizer


class TestAsyncAI21Tokenizer:
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        ids=[
            "when_j2_tokenizer",
            "when_jamba_instruct_tokenizer",
        ],
        argnames=["tokenizer_name", "expected_tokens"],
        argvalues=[
            ("j2-tokenizer", 8),
            ("jamba-tokenizer", 9),
        ],
    )
    async def test__count_tokens__should_return_number_of_tokens(self, tokenizer_name: str, expected_tokens: int):
        tokenizer = await get_async_tokenizer(tokenizer_name)

        actual_number_of_tokens = await tokenizer.count_tokens("Text to Tokenize - Hello world!")

        assert actual_number_of_tokens == expected_tokens

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        ids=[
            "when_j2_tokenizer",
            "when_jamba_instruct_tokenizer",
        ],
        argnames=["tokenizer_name", "expected_tokens"],
        argvalues=[
            ("j2-tokenizer", ["▁Text", "▁to", "▁Token", "ize", "▁-", "▁Hello", "▁world", "!"]),
            (
                "jamba-tokenizer",
                ["<|startoftext|>", "Text", "▁to", "▁Token", "ize", "▁-", "▁Hello", "▁world", "!"],
            ),
        ],
    )
    async def test__tokenize__should_return_list_of_tokens(self, tokenizer_name: str, expected_tokens: List[str]):
        tokenizer = await get_async_tokenizer(tokenizer_name)

        actual_tokens = await tokenizer.tokenize("Text to Tokenize - Hello world!")

        assert actual_tokens == expected_tokens

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        ids=[
            "when_j2_tokenizer",
            "when_jamba_instruct_tokenizer",
        ],
        argnames=["tokenizer_name"],
        argvalues=[
            ("j2-tokenizer",),
            ("jamba-tokenizer",),
        ],
    )
    async def test__detokenize__should_return_list_of_tokens(self, tokenizer_name: str):
        tokenizer = await get_async_tokenizer(tokenizer_name)
        original_text = "Text to Tokenize - Hello world!"
        actual_tokens = await tokenizer.tokenize(original_text)
        detokenized_text = await tokenizer.detokenize(actual_tokens)

        assert original_text == detokenized_text

    @pytest.mark.asyncio
    async def test__tokenizer__should_be_singleton__when_called_twice(self):
        tokenizer1 = await get_async_tokenizer()
        tokenizer2 = await get_async_tokenizer()

        assert tokenizer1 is tokenizer2

    @pytest.mark.asyncio
    async def test__get_tokenizer__when_called_with_different_tokenizer_name__should_return_different_tokenizer(self):
        tokenizer1 = await get_async_tokenizer("j2-tokenizer")
        tokenizer2 = await get_async_tokenizer("jamba-tokenizer")

        assert tokenizer1._tokenizer is not tokenizer2._tokenizer

    @pytest.mark.asyncio
    async def test__get_tokenizer__when_tokenizer_name_not_supported__should_raise_error(self):
        with pytest.raises(ValueError):
            await get_async_tokenizer("some-tokenizer")
