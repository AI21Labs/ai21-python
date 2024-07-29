from typing import AsyncIterable, Iterable

import httpx
import pytest

from ai21.clients.bedrock._stream_decoder import AWSEventStreamDecoder
from ai21.errors import StreamingDecodeError
from ai21.models.chat import ChatCompletionChunk
from ai21.stream.async_stream import AsyncStream
from ai21.stream.stream import Stream


def byte_stream() -> Iterable[bytes]:
    for i in range(10):
        yield (
            b"\x00\x00\x01\x80\x00\x00\x00K\xfe\x96$F\x0b:event-type\x07\x00\x05chunk\r:content-type\x07\x00"
            b"\x10application/json\r:message-type\x07\x00\x05event{"
            b'"bytes":"eyJpZCI6ImNtcGwtOTgxZjdmMTc2YWQ0NDE0NTliOTRlNDVlZTI5MmEzMjEiLCJjaG9pY2VzIjpbeyJpbmRleC'
            b"I6MCwiZGVsdGEiOnsicm9sZSI6ImFzc2lzdGFudCJ9LCJmaW5pc2hfcmVhc29uIjpudWxsfV0sInVzYWdlIjp7InByb21wd"
            b'F90b2tlbnMiOjQ0LCJ0b3RhbF90b2tlbnMiOjQ0LCJjb21wbGV0aW9uX3Rva2VucyI6MH19","p":"abcdefghijklmnopq'
            b'rstuv"}5\xca\xa7\x98'
        )


async def async_byte_stream() -> AsyncIterable[bytes]:
    for i in range(10):
        yield (
            b"\x00\x00\x01\x80\x00\x00\x00K\xfe\x96$F\x0b:event-type\x07\x00\x05chunk\r:content-type\x07\x00"
            b"\x10application/json\r:message-type\x07\x00\x05event{"
            b'"bytes":"eyJpZCI6ImNtcGwtOTgxZjdmMTc2YWQ0NDE0NTliOTRlNDVlZTI5MmEzMjEiLCJjaG9pY2VzIjpbeyJpbmRleC'
            b"I6MCwiZGVsdGEiOnsicm9sZSI6ImFzc2lzdGFudCJ9LCJmaW5pc2hfcmVhc29uIjpudWxsfV0sInVzYWdlIjp7InByb21wd"
            b'F90b2tlbnMiOjQ0LCJ0b3RhbF90b2tlbnMiOjQ0LCJjb21wbGV0aW9uX3Rva2VucyI6MH19","p":"abcdefghijklmnopq'
            b'rstuv"}5\xca\xa7\x98'
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
    stream_obj = Stream[ChatCompletionChunk](
        response=response, cast_to=ChatCompletionChunk, streaming_decoder=AWSEventStreamDecoder()
    )

    chunk_counter = 0
    for i, chunk in enumerate(stream_obj):
        assert isinstance(chunk, ChatCompletionChunk)
        chunk_counter += 1

    assert chunk_counter == 10


@pytest.mark.asyncio
async def test_async_stream_object_when_json_string_ok__should_be_ok():
    stream = async_byte_stream()
    response = httpx.Response(status_code=200, content=stream)
    stream_obj = AsyncStream[ChatCompletionChunk](
        response=response, cast_to=ChatCompletionChunk, streaming_decoder=AWSEventStreamDecoder()
    )

    chunk_counter = 0
    async for chunk in stream_obj:
        assert isinstance(chunk, ChatCompletionChunk)
        chunk_counter += 1

    assert chunk_counter == 10


def test_stream_object_when_bad_json__should_raise_error():
    stream = byte_bad_stream_json_format()
    response = httpx.Response(status_code=200, content=stream)
    stream_obj = Stream[ChatCompletionChunk](
        response=response, cast_to=ChatCompletionChunk, streaming_decoder=AWSEventStreamDecoder()
    )

    with pytest.raises(StreamingDecodeError):
        for _ in stream_obj:
            pass


@pytest.mark.asyncio
async def test_async_stream_object_when_bad_json__should_raise_error():
    stream = async_byte_bad_stream_json_format()
    response = httpx.Response(status_code=200, content=stream)
    stream_obj = AsyncStream[ChatCompletionChunk](
        response=response, cast_to=ChatCompletionChunk, streaming_decoder=AWSEventStreamDecoder()
    )

    with pytest.raises(StreamingDecodeError):
        async for _ in stream_obj:
            pass
