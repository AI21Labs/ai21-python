from typing import Dict

from ai21_tokenizer import Tokenizer, PreTrainedTokenizers

from ai21.tokenizers.ai21_tokenizer import AI21Tokenizer, AsyncAI21Tokenizer

_cached_tokenizers: Dict[str, AI21Tokenizer] = {}
_cached_async_tokenizers: Dict[str, AsyncAI21Tokenizer] = {}


def get_tokenizer(name: str = PreTrainedTokenizers.J2_TOKENIZER) -> AI21Tokenizer:
    """
    Get the tokenizer instance.

    If the tokenizer instance is not cached, it will be created using the Tokenizer.get_tokenizer() method.
    """
    global _cached_tokenizers

    if _cached_tokenizers.get(name) is None:
        _cached_tokenizers[name] = AI21Tokenizer(Tokenizer.get_tokenizer(name))

    return _cached_tokenizers[name]


async def get_async_tokenizer(name: str = PreTrainedTokenizers.J2_TOKENIZER) -> AsyncAI21Tokenizer:
    """
    Get the async tokenizer instance.

    If the tokenizer instance is not cached, it will be created using the Tokenizer.get_tokenizer() method.
    """
    global _cached_async_tokenizers

    if _cached_async_tokenizers.get(name) is None:
        _cached_async_tokenizers[name] = AsyncAI21Tokenizer(await Tokenizer.get_async_tokenizer(name))

    return _cached_async_tokenizers[name]
