from __future__ import annotations

import json
from types import TracebackType
from typing import TypeVar, Generic, Iterator, Optional

import httpx
from typing_extensions import Self

from ai21.errors import StreamingDecodeError

_T = TypeVar("_T")
_SSE_DATA_PREFIX = "data: "
_SSE_DONE_MSG = "[DONE]"


class Stream(Generic[_T]):
    response: httpx.Response

    def __init__(
        self,
        *,
        cast_to: type[_T],
        response: httpx.Response,
    ):
        self.response = response
        self.cast_to = cast_to
        self._decoder = _SSEDecoder()
        self._iterator = self.__stream__()

    def __next__(self) -> _T:
        return self._iterator.__next__()

    def __iter__(self) -> Iterator[_T]:
        for item in self._iterator:
            yield item

    def __stream__(self) -> Iterator[_T]:
        for chunk in self._decoder.iter(self.response.iter_lines()):
            if chunk.endswith(_SSE_DONE_MSG):
                break

            try:
                chunk = json.loads(chunk)
                if hasattr(self.cast_to, "from_dict"):
                    yield self.cast_to.from_dict(chunk)
                else:
                    yield self.cast_to(**chunk)
            except json.JSONDecodeError:
                raise StreamingDecodeError(chunk)

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()

    def close(self):
        self.response.close()


class _SSEDecoder:
    def iter(self, iterator: Iterator[str]):
        for line in iterator:
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
