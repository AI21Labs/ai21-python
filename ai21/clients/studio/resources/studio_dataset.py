from typing import Optional, List

from ai21.clients.common.dataset_base import Dataset
from ai21.models.responses.dataset_response import DatasetResponse
from ai21.clients.studio.resources.studio_resource import StudioResource


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
        )
        return self._post(
            url=self._base_url(),
            body=body,
            files=files,
        )

    def list(self) -> List[DatasetResponse]:
        response = self._get(url=self._base_url())
        return [self._json_to_response(r) for r in response]

    def get(self, dataset_pid: str) -> DatasetResponse:
        url = f"{self._base_url()}/{dataset_pid}"
        response = self._get(url=url)

        return self._json_to_response(response)

    def _base_url(self) -> str:
        return f"{self._client.get_base_url()}/{self._module_name}"
