from __future__ import annotations

from functools import lru_cache
from typing import Iterator, AsyncIterator

import httpx
from botocore.eventstream import EventStreamMessage
from botocore.model import Shape

from ai21.errors import StreamingDecodeError


@lru_cache(maxsize=None)
def get_response_stream_shape() -> Shape:
    from botocore.model import ServiceModel
    from botocore.loaders import Loader

    loader = Loader()
    bedrock_service_dict = loader.load_service_model("bedrock-runtime", "service-2")
    bedrock_service_model = ServiceModel(bedrock_service_dict)
    return bedrock_service_model.shape_for("ResponseStream")


class AWSEventStreamDecoder:
    def __init__(self) -> None:
        from botocore.parsers import EventStreamJSONParser

        self.parser = EventStreamJSONParser()

    def iter(self, response: httpx.Response) -> Iterator[str]:
        """Given an iterator that yields lines, iterate over it & yield every event encountered"""
        from botocore.eventstream import EventStreamBuffer

        event_stream_buffer = EventStreamBuffer()
        for chunk in response.iter_bytes():
            try:
                event_stream_buffer.add_data(chunk)
                for event in event_stream_buffer:
                    message = self._parse_message_from_event(event)
                    if message:
                        yield message
            except Exception as e:
                raise StreamingDecodeError(chunk=str(chunk), error_message=str(e))

    async def aiter(self, response: httpx.Response) -> AsyncIterator[str]:
        """Given an async iterator that yields lines, iterate over it & yield every event encountered"""
        from botocore.eventstream import EventStreamBuffer

        event_stream_buffer = EventStreamBuffer()
        async for chunk in response.aiter_bytes():
            try:
                event_stream_buffer.add_data(chunk)
                for event in event_stream_buffer:
                    message = self._parse_message_from_event(event)
                    if message:
                        yield message
            except Exception as e:
                raise StreamingDecodeError(chunk=str(chunk), error_message=str(e))

    def _parse_message_from_event(self, event: EventStreamMessage) -> str | None:
        response_dict = event.to_response_dict()
        parsed_response = self.parser.parse(response_dict, get_response_stream_shape())
        if response_dict["status_code"] != 200:
            raise ValueError(f"Bad response code, expected 200: {response_dict}")

        chunk = parsed_response.get("chunk")
        if not chunk:
            return None

        return chunk.get("bytes").decode()  # type: ignore[no-any-return]
