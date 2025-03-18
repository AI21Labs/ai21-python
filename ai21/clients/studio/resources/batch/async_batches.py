from os import PathLike
from typing import Any, Dict, Literal, Optional

from ai21.clients.studio.resources.batch.base_batches import BaseBatches
from ai21.clients.studio.resources.studio_resource import AsyncStudioResource
from ai21.files.downloaded_file import DownloadedFile
from ai21.models.responses.batch_response import Batch
from ai21.pagination.async_pagination import AsyncPagination
from ai21.types import NOT_GIVEN, NotGiven


class AsyncBatches(AsyncStudioResource, BaseBatches):
    async def create(
        self,
        file: PathLike,
        endpoint: Literal["/v1/chat/completions"],
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ):
        files = {"file": open(file, "rb")}
        body = self._create_body(endpoint=endpoint, metadata=metadata, **kwargs)

        return await self._post(path=f"/{self._module_name}", files=files, body=body, response_cls=dict)

    async def retrieve(self, batch_id: str):
        return await self._get(path=f"/{self._module_name}/{batch_id}", response_cls=dict)

    async def list(
        self,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
    ) -> AsyncPagination[Batch]:
        params = self._create_list_params(after=after, limit=limit)
        return await self._list(
            path=f"/{self._module_name}",
            params=params,
            page_cls=AsyncPagination[Batch],
            response_cls=Batch,
        )

    async def cancel(self, batch_id: str):
        return await self._post(path=f"/{self._module_name}/{batch_id}/cancel", response_cls=dict)

    async def get_results(
        self,
        batch_id: str,
        file_type: Literal["output", "error"],
        force: bool = False,
        **kwargs: Any,
    ) -> DownloadedFile:
        return await self._get(
            path=f"/{self._module_name}/{batch_id}/results",
            params={"file_type": file_type, "force": force},
            response_cls=DownloadedFile,
            **kwargs,
        )
