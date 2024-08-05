from __future__ import annotations

import json
from functools import lru_cache
from typing import Iterator, AsyncIterator

import httpx
from botocore.eventstream import EventStreamMessage, EventStreamBuffer
from botocore.model import Shape
from botocore.parsers import EventStreamJSONParser

from ai21.errors import StreamingDecodeError
from ai21.stream.stream_commons import _SSEDecoderBase


_FINISH_REASON_NULL_STR = '"finish_reason":null'


@lru_cache(maxsize=None)
def get_response_stream_shape() -> Shape:
    from botocore.model import ServiceModel
    from botocore.loaders import Loader

    loader = Loader()
    bedrock_service_dict = loader.load_service_model("bedrock-runtime", "service-2")
    bedrock_service_model = ServiceModel(bedrock_service_dict)
    return bedrock_service_model.shape_for("ResponseStream")


class _AWSEventStreamDecoder(_SSEDecoderBase):
    def __init__(self) -> None:
        self._parser = EventStreamJSONParser()

    def iter(self, response: httpx.Response) -> Iterator[str]:
        event_stream_buffer = EventStreamBuffer()
        previous_item = None
        for chunk in response.iter_bytes():
            try:
                item = next(self._process_chunks(event_stream_buffer, chunk))
            except StopIteration as e:
                raise StreamingDecodeError(chunk=str(chunk), error_message=str(e))
            # For Bedrock metering chunk:
            if previous_item is not None:
                item = self._build_last_chunk(last_model_chunk=previous_item, bedrock_metrics_chunk=item)
            if _FINISH_REASON_NULL_STR not in item and previous_item is None:
                previous_item = item
                continue
            yield item

    async def aiter(self, response: httpx.Response) -> AsyncIterator[str]:
        event_stream_buffer = EventStreamBuffer()
        previous_item = None
        async for chunk in response.aiter_bytes():
            try:
                item = next(self._process_chunks(event_stream_buffer, chunk))
            except StopIteration as e:
                raise StreamingDecodeError(chunk=str(chunk), error_message=str(e))
            # For Bedrock metering chunk:
            if previous_item is not None:
                item = self._build_last_chunk(last_model_chunk=previous_item, bedrock_metrics_chunk=item)
            if _FINISH_REASON_NULL_STR not in item and previous_item is None:
                previous_item = item
                continue
            yield item

    def _parse_message_from_event(self, event: EventStreamMessage) -> str | None:
        response_dict = event.to_response_dict()
        parsed_response = self._parser.parse(response_dict, get_response_stream_shape())
        if response_dict["status_code"] != 200:
            raise ValueError(f"Bad response code, expected 200: {response_dict}")

        chunk = parsed_response.get("chunk")
        if not chunk:
            return None

        return chunk.get("bytes").decode()  # type: ignore[no-any-return]

    def _build_last_chunk(self, last_model_chunk: str, bedrock_metrics_chunk: str) -> str:
        chunk_dict = json.loads(last_model_chunk)
        bedrock_metrics_dict = json.loads(bedrock_metrics_chunk)
        chunk_dict = {**chunk_dict, **bedrock_metrics_dict}
        return json.dumps(chunk_dict)

    def _process_chunks(self, event_stream_buffer, chunk) -> Iterator[str]:
        try:
            event_stream_buffer.add_data(chunk)
            for event in event_stream_buffer:
                message = self._parse_message_from_event(event)
                if message:
                    yield message
        except Exception as e:
            raise StreamingDecodeError(chunk=str(chunk), error_message=str(e))
