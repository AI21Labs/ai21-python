from __future__ import annotations

from types import TracebackType
from typing import Generic, Iterator, Optional, Any

import httpx
from typing_extensions import Self

from ai21.stream.stream_commons import _T, _SSEDecoder, _SSE_DONE_MSG, get_stream_message


class Stream(Generic[_T]):
    response: httpx.Response

    def __init__(
        self,
        *,
        cast_to: type[_T],
        response: httpx.Response,
        streaming_decoder: Optional[Any] = None,
    ):
        self.response = response
        self.cast_to = cast_to
        self._decoder = streaming_decoder or _SSEDecoder()
        self._iterator = self.__stream__()

    def __next__(self) -> _T:
        return self._iterator.__next__()

    def __iter__(self) -> Iterator[_T]:
        for item in self._iterator:
            yield item

    def __stream__(self) -> Iterator[_T]:
        iterator = self._decoder.iter(self.response)
        for chunk in iterator:
            if chunk.endswith(_SSE_DONE_MSG):
                break

            yield get_stream_message(chunk, self.cast_to)

        # Ensure the entire stream is consumed
        for _chunk in iterator:
            ...

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
