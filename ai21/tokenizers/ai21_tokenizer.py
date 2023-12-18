from typing import List

from ai21_tokenizer import BaseTokenizer


class AI21Tokenizer:
    """
    A class that wraps a tokenizer and provides additional functionality.
    """

    def __init__(self, tokenizer: BaseTokenizer):
        self._tokenizer = tokenizer

    def count_tokens(self, text: str) -> int:
        encoded_text = self._tokenizer.encode(text)

        return len(encoded_text)

    def tokenize(self, text: str) -> List[str]:
        encoded_text = self._tokenizer.encode(text)

        return self._tokenizer.convert_ids_to_tokens(encoded_text)
