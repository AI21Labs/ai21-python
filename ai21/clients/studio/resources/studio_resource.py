from __future__ import annotations

import json
from abc import ABC
from typing import Any, Dict, Optional, BinaryIO, get_origin

import httpx

from ai21.ai21_http_client import AI21HTTPClient

from ai21.types import ResponseT, StreamT
from ai21.utils.typing import extract_type


class StudioResource(ABC):
    def __init__(self, client: AI21HTTPClient):
        self._client = client

    def _post(
        self,
        url: str,
        body: Dict[str, Any],
        response_cls: Optional[ResponseT] = None,
        stream_cls: Optional[StreamT] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
    ) -> ResponseT | StreamT:
        response = self._client.execute_http_request(
            method="POST",
            url=url,
            stream=stream,
            params=body or {},
            files=files,
        )

        return self._cast_response(stream=stream, response=response, response_cls=response_cls, stream_cls=stream_cls)

    def _get(
        self, url: str, response_cls: Optional[ResponseT] = None, params: Optional[Dict[str, Any]] = None
    ) -> ResponseT | StreamT:
        response = self._client.execute_http_request(method="GET", url=url, params=params or {})
        return self._cast_response(response=response, response_cls=response_cls)

    def _put(
        self, url: str, response_cls: Optional[ResponseT] = None, body: Dict[str, Any] = None
    ) -> ResponseT | StreamT:
        response = self._client.execute_http_request(method="PUT", url=url, params=body or {})
        return self._cast_response(response=response, response_cls=response_cls)

    def _delete(self, url: str, response_cls: Optional[ResponseT] = None) -> ResponseT | StreamT:
        response = self._client.execute_http_request(
            method="DELETE",
            url=url,
        )
        return self._cast_response(response=response, response_cls=response_cls)

    def _cast_response(
        self,
        response: httpx.Response,
        response_cls: Optional[ResponseT],
        stream_cls: Optional[StreamT] = None,
        stream: bool = False,
    ) -> ResponseT | StreamT | None:
        if stream and stream_cls is not None:
            cast_to = extract_type(stream_cls)
            return stream_cls(cast_to=cast_to, response=response)

        if response_cls is None:
            return None

        if response_cls == dict:
            return response.json()

        if response_cls == str:
            return json.loads(response.json())

        origin_type = get_origin(response_cls)

        if origin_type is not None and origin_type == list:
            subtype = extract_type(response_cls)
            return [subtype.from_dict(item) for item in response.json()]

        return response_cls.from_dict(response.json())
