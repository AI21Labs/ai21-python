from typing import Optional, List

from ai21.clients.common.dataset_base import Dataset
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import DatasetResponse


class StudioDataset(StudioResource, Dataset):
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

    def list(self) -> List[DatasetResponse]:
        return self._get(path=f"/{self._module_name}", response_cls=List[DatasetResponse])

    def get(self, dataset_pid: str) -> DatasetResponse:
        return self._get(path=f"/{self._module_name}/{dataset_pid}", response_cls=DatasetResponse)


class AsyncStudioDataset(AsyncStudioResource, Dataset):
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

    async def list(self) -> List[DatasetResponse]:
        return await self._get(path=f"/{self._module_name}", response_cls=List[DatasetResponse])

    async def get(self, dataset_pid: str) -> DatasetResponse:
        return await self._get(path=f"/{self._module_name}/{dataset_pid}", response_cls=DatasetResponse)
