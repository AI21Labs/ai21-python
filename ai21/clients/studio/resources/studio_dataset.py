from typing import Optional, List

from ai21.clients.common.dataset_base import Dataset
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import DatasetResponse
from ai21.version_utils import V3_DEPRECATION_MESSAGE, deprecated


class StudioDataset(StudioResource, Dataset):
    @deprecated(V3_DEPRECATION_MESSAGE)
    def create(
        self,
        file_path: str,
        dataset_name: str,
        *,
        selected_columns: Optional[str] = None,
        approve_whitespace_correction: Optional[bool] = None,
        delete_long_rows: Optional[bool] = None,
        split_ratio: Optional[float] = None,
        **kwargs,
    ):
        files = {"dataset_file": open(file_path, "rb")}
        body = self._create_body(
            dataset_name=dataset_name,
            selected_columns=selected_columns,
            approve_whitespace_correction=approve_whitespace_correction,
            delete_long_rows=delete_long_rows,
            split_ratio=split_ratio,
            **kwargs,
        )
        return self._post(
            path=f"/{self._module_name}",
            body=body,
            files=files,
        )

    @deprecated(V3_DEPRECATION_MESSAGE)
    def list(self) -> List[DatasetResponse]:
        return self._get(path=f"/{self._module_name}", response_cls=List[DatasetResponse])

    @deprecated(V3_DEPRECATION_MESSAGE)
    def get(self, dataset_pid: str) -> DatasetResponse:
        return self._get(path=f"/{self._module_name}/{dataset_pid}", response_cls=DatasetResponse)


class AsyncStudioDataset(AsyncStudioResource, Dataset):
    @deprecated(V3_DEPRECATION_MESSAGE)
    async def create(
        self,
        file_path: str,
        dataset_name: str,
        *,
        selected_columns: Optional[str] = None,
        approve_whitespace_correction: Optional[bool] = None,
        delete_long_rows: Optional[bool] = None,
        split_ratio: Optional[float] = None,
        **kwargs,
    ):
        files = {"dataset_file": open(file_path, "rb")}
        body = self._create_body(
            dataset_name=dataset_name,
            selected_columns=selected_columns,
            approve_whitespace_correction=approve_whitespace_correction,
            delete_long_rows=delete_long_rows,
            split_ratio=split_ratio,
            **kwargs,
        )

        return await self._post(
            path=f"/{self._module_name}",
            body=body,
            files=files,
        )

    @deprecated(V3_DEPRECATION_MESSAGE)
    async def list(self) -> List[DatasetResponse]:
        return await self._get(path=f"/{self._module_name}", response_cls=List[DatasetResponse])

    @deprecated(V3_DEPRECATION_MESSAGE)
    async def get(self, dataset_pid: str) -> DatasetResponse:
        return await self._get(path=f"/{self._module_name}/{dataset_pid}", response_cls=DatasetResponse)
