from __future__ import annotations

from os import PathLike
from typing import Any, Dict, Literal

from ai21.clients.studio.resources.batch.base_batches import BaseBatches
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.files.downloaded_file import DownloadedFile
from ai21.models.responses.batch_response import Batch
from ai21.pagination.sync_pagination import SyncPagination
from ai21.types import NOT_GIVEN, NotGiven


class Batches(StudioResource, BaseBatches):
    def create(
        self,
        file: str | PathLike[str],
        endpoint: Literal["/v1/chat/completions"],
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> Batch:
        files = {"file": open(file, "rb")}
        body = self._create_body(endpoint=endpoint, metadata=metadata, **kwargs)

        return self._post(path=f"/{self._module_name}", files=files, body=body, response_cls=Batch)

    def retrieve(self, batch_id: str) -> Batch:
        return self._get(path=f"/{self._module_name}/{batch_id}", response_cls=Batch)

    def list(
        self,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> SyncPagination[Batch]:
        """List your organization's batches.

        Args:
            after: A cursor for pagination. Provide a batch ID to fetch results
                  starting after this batch. Useful for navigating through large
                  result sets.

            limit: Maximum number of batches to return per page. Value must be
                  between 1 and 100. Defaults to 20 if not specified.

        Returns:
            A paginator object that yields pages of batch results when iterated.
        """
        params = self._create_list_params(after=after, limit=limit)
        return self._list(
            path=f"/{self._module_name}",
            params=params,
            pagination_cls=SyncPagination[Batch],
            response_cls=Batch,
            **kwargs,
        )

    def cancel(self, batch_id: str) -> Batch:
        return self._post(path=f"/{self._module_name}/{batch_id}/cancel", response_cls=dict)

    def get_results(
        self,
        batch_id: str,
        file_type: Literal["output", "error"] | NotGiven = NOT_GIVEN,
        force: bool | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> DownloadedFile:
        return self._get(
            path=f"/{self._module_name}/{batch_id}/results",
            params={"file_type": file_type, "force": force},
            response_cls=DownloadedFile,
            **kwargs,
        )
