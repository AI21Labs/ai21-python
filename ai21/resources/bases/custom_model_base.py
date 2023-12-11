from abc import ABC, abstractmethod
from typing import Optional, List, Any, Dict

from ai21.resources.responses.custom_model_response import CustomModelResponse


class CustomModel(ABC):
    _module_name = "custom-model"

    @abstractmethod
    def create(
        self,
        dataset_id: str,
        model_name: str,
        model_type: str,
        *,
        learning_rate: Optional[float] = None,
        num_epochs: Optional[int] = None,
        **kwargs,
    ) -> None:
        pass

    @abstractmethod
    def list(self) -> List[CustomModelResponse]:
        pass

    @abstractmethod
    def get(self, resource_id: str) -> CustomModelResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> CustomModelResponse:
        return CustomModelResponse.model_validate(json)
