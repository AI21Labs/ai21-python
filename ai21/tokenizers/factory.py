from typing import Optional

from ai21_tokenizer import Tokenizer

from ai21.tokenizers.ai21_tokenizer import AI21Tokenizer

_cached_tokenizer: Optional[AI21Tokenizer] = None


def get_tokenizer() -> AI21Tokenizer:
    """
    Get the tokenizer instance.

    If the tokenizer instance is not cached, it will be created using the Tokenizer.get_tokenizer() method.
    """
    global _cached_tokenizer

    if _cached_tokenizer is None:
        _cached_tokenizer = AI21Tokenizer(Tokenizer.get_tokenizer())

    return _cached_tokenizer
