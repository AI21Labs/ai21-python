from __future__ import annotations

import json

from abc import ABC
from typing import Any, BinaryIO, Callable, Dict, Optional, get_origin

import httpx

from ai21.files.downloaded_file import DownloadedFile
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models._pydantic_compatibility import _from_dict
from ai21.stream.stream_commons import _SSEDecoderBase
from ai21.types import AsyncPaginationT, AsyncStreamT, PaginationT, ResponseT, StreamT
from ai21.utils.typing import extract_type


def _cast_response(
    response: httpx.Response,
    response_cls: Optional[ResponseT],
    stream_cls: Optional[StreamT | AsyncStreamT] = None,
    stream: bool = False,
    streaming_decoder: Optional[_SSEDecoderBase] = None,
) -> ResponseT | StreamT | None:
    if stream and stream_cls is not None:
        cast_to = extract_type(stream_cls)
        return stream_cls(cast_to=cast_to, response=response, streaming_decoder=streaming_decoder)

    if response_cls is DownloadedFile:
        return DownloadedFile(response)

    if response_cls is None:
        return None

    if response_cls == dict:
        return response.json()

    if response_cls == str:
        return json.loads(response.json())

    origin_type = get_origin(response_cls)

    if origin_type is not None and origin_type == list:
        subtype = extract_type(response_cls)
        return [_from_dict(obj=subtype, obj_dict=item) for item in response.json()]

    return _from_dict(obj=response_cls, obj_dict=response.json())


def _cast_request(
    request_callback: Callable,
    path: str,
    params: Optional[Dict[str, Any]],
    response_cls: Optional[ResponseT],
    page_cls: PaginationT | AsyncPaginationT,
    **kwargs: Any,
) -> PaginationT | AsyncPaginationT:
    return page_cls(
        request_callback=request_callback,
        path=path,
        params=params,
        response_cls=response_cls,
        **kwargs,
    )


class StudioResource(ABC):
    def __init__(self, client: AI21HTTPClient):
        self._client = client

    def _list(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        response_cls: Optional[ResponseT] = None,
        page_cls: Optional[PaginationT] = None,
        **kwargs: Any,
    ) -> ResponseT | PaginationT | None:
        if page_cls is not None:
            return _cast_request(
                request_callback=self._client.execute_http_request,
                path=path,
                params=params,
                response_cls=response_cls,
                page_cls=page_cls,
                **kwargs,
            )

        response = self._client.execute_http_request(
            method="GET",
            path=path,
            params=params or {},
            **kwargs,
        )

        return _cast_response(
            response=response,
            response_cls=response_cls,
        )

    def _post(
        self,
        path: str,
        body: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        response_cls: Optional[ResponseT] = None,
        stream_cls: Optional[StreamT] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
    ) -> ResponseT | StreamT | None:
        response = self._client.execute_http_request(
            method="POST",
            path=path,
            stream=stream,
            body=body or {},
            params=params or {},
            files=files,
        )

        return _cast_response(
            stream=stream,
            response=response,
            response_cls=response_cls,
            stream_cls=stream_cls,
            streaming_decoder=self._client._get_streaming_decoder(),
        )

    def _get(
        self,
        path: str,
        response_cls: Optional[ResponseT] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> ResponseT | StreamT:
        response = self._client.execute_http_request(method="GET", path=path, params=params or {})
        return _cast_response(response=response, response_cls=response_cls)

    def _put(
        self, path: str, response_cls: Optional[ResponseT] = None, body: Dict[str, Any] = None
    ) -> ResponseT | StreamT:
        response = self._client.execute_http_request(method="PUT", path=path, body=body or {})
        return _cast_response(response=response, response_cls=response_cls)

    def _delete(self, path: str, response_cls: Optional[ResponseT] = None) -> ResponseT | StreamT:
        response = self._client.execute_http_request(
            method="DELETE",
            path=path,
        )
        return _cast_response(response=response, response_cls=response_cls)


class AsyncStudioResource(ABC):
    def __init__(self, client: AsyncAI21HTTPClient):
        self._client = client

    async def _post(
        self,
        path: str,
        body: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        response_cls: Optional[ResponseT] = None,
        stream_cls: Optional[AsyncStreamT] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
    ) -> ResponseT | AsyncStreamT:
        response = await self._client.execute_http_request(
            method="POST",
            path=path,
            stream=stream,
            body=body or {},
            params=params or {},
            files=files,
        )

        return _cast_response(
            stream=stream,
            response=response,
            response_cls=response_cls,
            stream_cls=stream_cls,
            streaming_decoder=self._client._get_streaming_decoder(),
        )

    async def _get(
        self, path: str, response_cls: Optional[ResponseT] = None, params: Optional[Dict[str, Any]] = None
    ) -> ResponseT | AsyncStreamT:
        response = await self._client.execute_http_request(method="GET", path=path, params=params or {})
        return _cast_response(response=response, response_cls=response_cls)

    async def _put(
        self, path: str, response_cls: Optional[ResponseT] = None, body: Dict[str, Any] = None
    ) -> ResponseT | AsyncStreamT:
        response = await self._client.execute_http_request(method="PUT", path=path, body=body or {})
        return _cast_response(response=response, response_cls=response_cls)

    async def _delete(self, path: str, response_cls: Optional[ResponseT] = None) -> ResponseT | AsyncStreamT:
        response = await self._client.execute_http_request(
            method="DELETE",
            path=path,
        )
        return _cast_response(response=response, response_cls=response_cls)

    async def _list(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        response_cls: Optional[ResponseT] = None,
        page_cls: Optional[AsyncPaginationT] = None,
    ) -> ResponseT | AsyncPaginationT | None:
        if page_cls is not None:
            return _cast_request(
                request_callback=self._client.execute_http_request,
                path=path,
                params=params,
                response_cls=response_cls,
                page_cls=page_cls,
            )

        response = await self._client.execute_http_request(
            method="GET",
            path=path,
            params=params or {},
        )

        return _cast_response(
            response=response,
            response_cls=response_cls,
        )
