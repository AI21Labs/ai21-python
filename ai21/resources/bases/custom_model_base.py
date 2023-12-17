from abc import ABC, abstractmethod
from typing import Optional, List, Any, Dict

from ai21.resources.responses.custom_model_response import CustomBaseModelResponse


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
    def list(self) -> List[CustomBaseModelResponse]:
        pass

    @abstractmethod
    def get(self, resource_id: str) -> CustomBaseModelResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> CustomBaseModelResponse:
        return CustomBaseModelResponse.from_dict(json)

    def _create_body(
        self,
        dataset_id: str,
        model_name: str,
        model_type: str,
        learning_rate: Optional[float],
        num_epochs: Optional[int],
    ) -> Dict[str, Any]:
        return {
            "dataset_id": dataset_id,
            "model_name": model_name,
            "model_type": model_type,
            "learning_rate": learning_rate,
            "num_epochs": num_epochs,
        }
