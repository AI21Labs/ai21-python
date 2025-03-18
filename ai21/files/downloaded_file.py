from __future__ import annotations

import os

from typing import Iterator

import httpx


class DownloadedFile:
    def __init__(self, httpx_response: httpx.Response):
        self._response = httpx_response

    @property
    def content(self) -> bytes:
        return self._response.content

    def read(self) -> bytes:
        return self._response.read()

    def iter_bytes(self, chunk_size: int | None = None) -> Iterator[bytes]:
        return self._response.iter_bytes(chunk_size)

    def iter_text(self, chunk_size: int | None = None) -> Iterator[str]:
        return self._response.iter_text(chunk_size)

    def iter_lines(self) -> Iterator[str]:
        return self._response.iter_lines()

    def write_to_file(self, path: str | os.PathLike[str]):
        with open(path, "wb") as f:
            for data in self._response.iter_bytes():
                f.write(data)
