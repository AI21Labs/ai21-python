from typing import List, Any

from ai21_tokenizer import BaseTokenizer, AsyncBaseTokenizer


class AI21Tokenizer:
    """
    A class that wraps a tokenizer and provides additional functionality.
    """

    def __init__(self, tokenizer: BaseTokenizer):
        self._tokenizer = tokenizer

    def count_tokens(self, text: str) -> int:
        encoded_text = self._tokenizer.encode(text)

        return len(encoded_text)

    def tokenize(self, text: str, **kwargs: Any) -> List[str]:
        encoded_text = self._tokenizer.encode(text, **kwargs)

        return self._tokenizer.convert_ids_to_tokens(encoded_text, **kwargs)

    def detokenize(self, tokens: List[str], **kwargs: Any) -> str:
        token_ids = self._tokenizer.convert_tokens_to_ids(tokens)

        return self._tokenizer.decode(token_ids, **kwargs)


class AsyncAI21Tokenizer:
    """
    A class that wraps an async tokenizer and provides additional functionality.
    """

    def __init__(self, tokenizer: AsyncBaseTokenizer):
        self._tokenizer = tokenizer

    async def count_tokens(self, text: str) -> int:
        encoded_text = await self._tokenizer.encode(text)

        return len(encoded_text)

    async def tokenize(self, text: str, **kwargs: Any) -> List[str]:
        encoded_text = await self._tokenizer.encode(text, **kwargs)

        return await self._tokenizer.convert_ids_to_tokens(encoded_text, **kwargs)

    async def detokenize(self, tokens: List[str], **kwargs: Any) -> str:
        token_ids = await self._tokenizer.convert_tokens_to_ids(tokens)

        return await self._tokenizer.decode(token_ids, **kwargs)
