from __future__ import annotations

from abc import ABC
from typing import Any, Dict, Optional, BinaryIO

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
        response_cls: ResponseT,
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

    def _get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._client.execute_http_request(method="GET", url=url, params=params or {})

    def _put(self, url: str, body: Dict[str, Any] = None) -> Dict[str, Any]:
        return self._client.execute_http_request(method="PUT", url=url, params=body or {})

    def _delete(self, url: str) -> Dict[str, Any]:
        return self._client.execute_http_request(
            method="DELETE",
            url=url,
        )

    def _cast_response(
        self,
        stream: bool,
        response: httpx.Response,
        response_cls: ResponseT,
        stream_cls: Optional[StreamT],
    ):
        if stream and stream_cls is not None:
            cast_to = extract_type(stream_cls)

            return stream_cls(
                cast_to=cast_to,
                response=response,
                client=self._client,
            )

        return response_cls.from_dict(response.json())
