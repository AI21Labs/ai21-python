from __future__ import annotations

from os import PathLike
from typing import List, Optional

from ai21.clients.studio.resources.studio_resource import (
    AsyncStudioResource,
    StudioResource,
)
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models import FileResponse
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class StudioLibrary(StudioResource):
    _module_name = "library/files"

    def __init__(self, client: AI21HTTPClient):
        super().__init__(client)
        self.files = LibraryFiles(client)


class LibraryFiles(StudioResource):
    _module_name = "library/files"

    def create(
        self,
        file_path: PathLike,
        *,
        path: Optional[str] | NotGiven = NOT_GIVEN,
        labels: Optional[List[str]] | NotGiven = NOT_GIVEN,
        public_url: Optional[str] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> str:
        files = {"file": open(file_path, "rb")}
        body = remove_not_given({"path": path, "labels": labels, "publicUrl": public_url, **kwargs})

        raw_response = self._post(path=f"/{self._module_name}", files=files, body=body, response_cls=dict)

        return raw_response["fileId"]

    def get(self, file_id: str) -> FileResponse:
        return self._get(path=f"/{self._module_name}/{file_id}", response_cls=FileResponse)

    def list(
        self,
        *,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> List[FileResponse]:
        params = remove_not_given({"offset": offset, "limit": limit})

        return self._get(path=f"/{self._module_name}", params=params, response_cls=List[FileResponse])

    def update(
        self,
        file_id: str,
        *,
        public_url: Optional[str] | NotGiven = NOT_GIVEN,
        labels: Optional[List[str]] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> None:
        body = remove_not_given(
            {
                "publicUrl": public_url,
                "labels": labels,
                **kwargs,
            }
        )
        self._put(path=f"/{self._module_name}/{file_id}", body=body)

    def delete(self, file_id: str) -> None:
        self._delete(path=f"/{self._module_name}/{file_id}")


class AsyncStudioLibrary(AsyncStudioResource):
    _module_name = "library/files"

    def __init__(self, client: AsyncAI21HTTPClient):
        super().__init__(client)
        self.files = AsyncLibraryFiles(client)


class AsyncLibraryFiles(AsyncStudioResource):
    _module_name = "library/files"

    async def create(
        self,
        file_path: str,
        *,
        path: Optional[str] | NotGiven = NOT_GIVEN,
        labels: Optional[List[str]] | NotGiven = NOT_GIVEN,
        public_url: Optional[str] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> str:
        files = {"file": open(file_path, "rb")}
        body = remove_not_given({"path": path, "labels": labels, "publicUrl": public_url, **kwargs})

        raw_response = await self._post(path=f"/{self._module_name}", files=files, body=body, response_cls=dict)

        return raw_response["fileId"]

    async def get(self, file_id: str) -> FileResponse:
        return await self._get(path=f"/{self._module_name}/{file_id}", response_cls=FileResponse)

    async def list(
        self,
        *,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> List[FileResponse]:
        params = remove_not_given({"offset": offset, "limit": limit})

        return await self._get(path=f"/{self._module_name}", params=params, response_cls=List[FileResponse])

    async def update(
        self,
        file_id: str,
        *,
        public_url: Optional[str] | NotGiven = NOT_GIVEN,
        labels: Optional[List[str]] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> None:
        body = remove_not_given(
            {
                "publicUrl": public_url,
                "labels": labels,
                **kwargs,
            }
        )
        await self._put(path=f"/{self._module_name}/{file_id}", body=body)

    async def delete(self, file_id: str) -> None:
        await self._delete(path=f"/{self._module_name}/{file_id}")
