import pytest
from ai21.tokenizers.factory import get_tokenizer


class TestAI21Tokenizer:
    def test__count_tokens__should_return_number_of_tokens(self):
        expected_number_of_tokens = 8
        tokenizer = get_tokenizer()

        actual_number_of_tokens = tokenizer.count_tokens("Text to Tokenize - Hello world!")

        assert actual_number_of_tokens == expected_number_of_tokens

    def test__tokenize__should_return_list_of_tokens(self):
        expected_tokens = ["▁Text", "▁to", "▁Token", "ize", "▁-", "▁Hello", "▁world", "!"]
        tokenizer = get_tokenizer()

        actual_tokens = tokenizer.tokenize("Text to Tokenize - Hello world!")

        assert actual_tokens == expected_tokens

    def test__tokenizer__should_be_singleton__when_called_twice(self):
        tokenizer1 = get_tokenizer()
        tokenizer2 = get_tokenizer()

        assert tokenizer1 is tokenizer2

    def test__get_tokenizer__when_called_with_different_tokenizer_name__should_return_different_tokenizer(self):
        tokenizer1 = get_tokenizer("j2-tokenizer")
        tokenizer2 = get_tokenizer("jamba-instruct-tokenizer")

        assert tokenizer1._tokenizer is not tokenizer2._tokenizer

    def test__get_tokenizer__when_tokenizer_name_not_supported__should_raise_error(self):
        with pytest.raises(ValueError):
            get_tokenizer("some-tokenizer")
