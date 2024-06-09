from __future__ import annotations

import json
from typing import TypeVar, Iterator, AsyncIterator, Optional
from ai21.errors import StreamingDecodeError


_T = TypeVar("_T")
_SSE_DATA_PREFIX = "data: "
_SSE_DONE_MSG = "[DONE]"


def get_stream_message(chunk: str, cast_to: type[_T]) -> Iterator[_T] | AsyncIterator[_T]:
    try:
        chunk = json.loads(chunk)
        if hasattr(cast_to, "from_dict"):
            return cast_to.from_dict(chunk)
        else:
            return cast_to(**chunk)
    except json.JSONDecodeError:
        raise StreamingDecodeError(chunk)


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
