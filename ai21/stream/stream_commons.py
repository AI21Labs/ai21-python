from __future__ import annotations

from typing import TypeVar, Iterator, AsyncIterator, Optional
from ai21.errors import StreamingDecodeError


_T = TypeVar("_T")
_SSE_DATA_PREFIX = "data: "
_SSE_DONE_MSG = "[DONE]"


class _SSEDecoder:
    def iter(self, iterator: Iterator[str]):
        for line in iterator:
            line = line.strip()
            decoded_line = self._decode(line)

            if decoded_line is not None:
                yield decoded_line

    async def aiter(self, iterator: AsyncIterator[str]):
        async for line in iterator:
            line = line.strip()
            decoded_line = self._decode(line)

            if decoded_line is not None:
                yield decoded_line

    def _decode(self, line: str) -> Optional[str]:
        if not line:
            return None

        if line.startswith(_SSE_DATA_PREFIX):
            return line.strip(_SSE_DATA_PREFIX)

        raise StreamingDecodeError(f"Invalid SSE line: {line}")
