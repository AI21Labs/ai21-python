from dataclasses import dataclass
from typing import AsyncIterable, Iterable, Optional, List

import httpx
import pytest

from ai21.clients.bedrock._stream_decoder import AWSEventStreamDecoder
from ai21.errors import StreamingDecodeError
from ai21.stream.async_stream import AsyncStream
from ai21.stream.stream import Stream


@dataclass
class TestChoiceDelta:
    content: Optional[str] = None
    role: Optional[str] = None


@dataclass
class TestChoicesChunk:
    index: int
    message: TestChoiceDelta
    finish_reason: Optional[str] = None


@dataclass
class TestChatCompletionChunk:
    choices: List[TestChoicesChunk]


def byte_stream() -> Iterable[bytes]:
    for i in range(10):
        yield (
            b"\x00\x00\x01\x0b\x00\x00\x00K8\xa0\xa5\xc5\x0b:event-type\x07\x00\x05chunk\r:content-type\x07\x00"
            b"\x10application/json\r:message-type\x07\x00\x05event{"
            b'"bytes":"eyJjaG9pY2VzIjpbeyJpbmRleCI6MCwibWVzc2FnZSI6eyJyb2xlIjoiYXNzaXN0YW50IiwiY29udGVudCI6Ikkif'
            b'Swic3RvcF9yZWFzb24iOm51bGx9XX0=","p":"abcdefghijklmnopqrstuvwxyzABCDEFGHIJK"}\x11\x061?'
        )


async def async_byte_stream() -> AsyncIterable[bytes]:
    for i in range(10):
        yield (
            b"\x00\x00\x01\x0b\x00\x00\x00K8\xa0\xa5\xc5\x0b:event-type\x07\x00\x05chunk\r:content-type\x07\x00"
            b"\x10application/json\r:message-type\x07\x00\x05event{"
            b'"bytes":"eyJjaG9pY2VzIjpbeyJpbmRleCI6MCwibWVzc2FnZSI6eyJyb2xlIjoiYXNzaXN0YW50IiwiY29udGVudCI6Ikkif'
            b'Swic3RvcF9yZWFzb24iOm51bGx9XX0=","p":"abcdefghijklmnopqrstuvwxyzABCDEFGHIJK"}\x11\x061?'
        )


def byte_bad_stream_json_format() -> AsyncIterable[bytes]:
    msg = "data: not a json format\r\n"
    yield msg.encode("utf-8")


async def async_byte_bad_stream_json_format() -> AsyncIterable[bytes]:
    msg = "data: not a json format\r\n"
    yield msg.encode("utf-8")


def test_stream_object_when_json_string_ok__should_be_ok():
    stream = byte_stream()
    response = httpx.Response(status_code=200, content=stream)
    stream_obj = Stream[TestChatCompletionChunk](
        response=response, cast_to=TestChatCompletionChunk, streaming_decoder=AWSEventStreamDecoder()
    )

    chunk_counter = 0
    for i, chunk in enumerate(stream_obj):
        assert isinstance(chunk, TestChatCompletionChunk)
        chunk_counter += 1

    assert chunk_counter == 10


@pytest.mark.asyncio
async def test_async_stream_object_when_json_string_ok__should_be_ok():
    stream = async_byte_stream()
    response = httpx.Response(status_code=200, content=stream)
    stream_obj = AsyncStream[TestChatCompletionChunk](
        response=response, cast_to=TestChatCompletionChunk, streaming_decoder=AWSEventStreamDecoder()
    )

    chunk_counter = 0
    async for chunk in stream_obj:
        assert isinstance(chunk, TestChatCompletionChunk)
        chunk_counter += 1

    assert chunk_counter == 10


def test_stream_object_when_bad_json__should_raise_error():
    stream = byte_bad_stream_json_format()
    response = httpx.Response(status_code=200, content=stream)
    stream_obj = Stream[TestChatCompletionChunk](
        response=response, cast_to=TestChatCompletionChunk, streaming_decoder=AWSEventStreamDecoder()
    )

    with pytest.raises(StreamingDecodeError):
        for _ in stream_obj:
            pass


@pytest.mark.asyncio
async def test_async_stream_object_when_bad_json__should_raise_error():
    stream = async_byte_bad_stream_json_format()
    response = httpx.Response(status_code=200, content=stream)
    stream_obj = AsyncStream[TestChatCompletionChunk](
        response=response, cast_to=TestChatCompletionChunk, streaming_decoder=AWSEventStreamDecoder()
    )

    with pytest.raises(StreamingDecodeError):
        async for _ in stream_obj:
            pass
