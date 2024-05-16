import json
from dataclasses import dataclass
from typing import AsyncIterable

import httpx
import pytest

from ai21.errors import StreamingDecodeError
from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin
from ai21.stream import Stream


@dataclass
class StubStreamObject(AI21BaseModelMixin):
    id: str
    name: str


def async_byte_stream() -> AsyncIterable[bytes]:
    for i in range(10):
        data = {"id": f"some-{i}", "name": f"some-name-{i}"}
        msg = f"data: {json.dumps(data)}\r\n"
        yield msg.encode("utf-8")


def async_byte_bad_stream_prefix() -> AsyncIterable[bytes]:
    msg = "bad_stream: {}\r\n"
    yield msg.encode("utf-8")


def async_byte_bad_stream_json_format() -> AsyncIterable[bytes]:
    msg = "data: not a json format\r\n"
    yield msg.encode("utf-8")


def test_stream_object_when_json_string_ok__should_be_ok():
    stream = async_byte_stream()
    response = httpx.Response(status_code=200, content=stream)
    stream_obj = Stream[StubStreamObject](response=response, cast_to=StubStreamObject)

    for i, chunk in enumerate(stream_obj):
        assert isinstance(chunk, StubStreamObject)
        assert chunk.name == f"some-name-{i}"
        assert chunk.id == f"some-{i}"


@pytest.mark.parametrize(
    ids=[
        "bad_stream_data_prefix",
        "bad_stream_json_format",
    ],
    argnames=["stream"],
    argvalues=[
        (async_byte_bad_stream_prefix(),),
        (async_byte_bad_stream_json_format(),),
    ],
)
def test_stream_object_when_bad_json__should_raise_error(stream):
    response = httpx.Response(status_code=200, content=stream)
    stream_obj = Stream[StubStreamObject](response=response, cast_to=StubStreamObject)

    with pytest.raises(StreamingDecodeError):
        for _ in stream_obj:
            pass
