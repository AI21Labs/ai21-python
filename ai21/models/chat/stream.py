import json
from typing import TypeVar, Generic, Iterator

import httpx

_T = TypeVar("_T")
_SSE_DATA_PREFIX = "data: "


class Stream(Generic[_T]):
    response: httpx.Response

    def __init__(
        self,
        *,
        cast_to: type[_T],
        response: httpx.Response,
        client,
    ):
        self.response = response
        self.client = client
        self.cast_to = cast_to
        self._decoder = SSEDecoder()
        self._iterator = self.__stream__()

    def __next__(self) -> _T:
        return self._iterator.__next__()

    def __iter__(self):
        for item in self._iterator:
            yield item

    def __stream__(self):
        for chunk in self._decoder.iter(self.response.iter_lines()):
            if chunk.endswith("[DONE]"):
                break

            chunk = json.loads(chunk)
            yield self.cast_to(**chunk)


class SSEDecoder:
    def iter(self, iterator: Iterator[str]):
        for line in iterator:
            line = line.strip()
            decoded_line = self._decode(line)
            if decoded_line is not None:
                yield decoded_line

    def _decode(self, line: str) -> str:
        if line.startswith(_SSE_DATA_PREFIX):
            return line.strip(_SSE_DATA_PREFIX)
