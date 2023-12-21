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
