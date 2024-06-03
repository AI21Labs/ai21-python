from abc import ABC, abstractmethod
from typing import Optional, Any, Dict


class Dataset(ABC):
    _module_name = "dataset"

    @abstractmethod
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
        """

        :param file_path: Local path to dataset
        :param dataset_name: Dataset name. Must be unique
        :param selected_columns: Mapping of the columns in the dataset file to prompt and completion columns.
        :param approve_whitespace_correction: Automatically correct examples that violate best practices
        :param delete_long_rows: Allow removal of examples where prompt + completion lengths exceeds 2047 tokens
        :param split_ratio:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def get(self, dataset_pid: str):
        pass

    def _create_body(
        self,
        dataset_name: str,
        selected_columns: Optional[str],
        approve_whitespace_correction: Optional[bool],
        delete_long_rows: Optional[bool],
        split_ratio: Optional[float],
        **kwargs,
    ) -> Dict[str, Any]:
        return {
            "dataset_name": dataset_name,
            "selected_columns": selected_columns,
            "approve_whitespace_correction": approve_whitespace_correction,
            "delete_long_rows": delete_long_rows,
            "split_ratio": split_ratio,
            **kwargs,
        }

    def _base_url(self, base_url: str) -> str:
        return f"{base_url}/{self._module_name}"
