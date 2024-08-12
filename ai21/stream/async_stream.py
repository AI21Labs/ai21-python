from __future__ import annotations

from typing import Generic, AsyncIterator, Optional, Any
from typing_extensions import Self
from types import TracebackType

from ai21.stream.stream_commons import _T, _SSEDecoder, _SSE_DONE_MSG, get_stream_message

import httpx


class AsyncStream(Generic[_T]):
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

    async def __anext__(self) -> _T:
        return await self._iterator.__anext__()

    async def __aiter__(self) -> AsyncIterator[_T]:
        async for item in self._iterator:
            yield item

    async def __stream__(self) -> AsyncIterator[_T]:
        iterator = self._decoder.aiter(self.response)
        async for chunk in iterator:
            if chunk.endswith(_SSE_DONE_MSG):
                break

            yield get_stream_message(chunk, self.cast_to)

        # Ensure the entire stream is consumed
        async for _chunk in iterator:
            ...

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()

    async def close(self):
        await self.response.aclose()
