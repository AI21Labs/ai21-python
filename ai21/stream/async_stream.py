from __future__ import annotations

from typing import Generic, AsyncIterator
from typing_extensions import Self
from types import TracebackType

from ai21.stream.stream_commons import _T, _SSEDecoder, _SSE_DONE_MSG, StreamingDecodeError

import httpx
import json


class AsyncStream(Generic[_T]):
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

    async def __anext__(self) -> _T:
        return await self._iterator.__anext__()

    async def __aiter__(self) -> AsyncIterator[_T]:
        async for item in self._iterator:
            yield item

    async def __stream__(self) -> AsyncIterator[_T]:
        async for chunk in self._decoder.aiter(self.response.aiter_lines()):
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
