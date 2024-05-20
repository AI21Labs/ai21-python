from abc import ABC, abstractmethod
from typing import Optional, List, Any, Dict

from ai21.models import CustomBaseModelResponse


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
        """

        :param dataset_id: The dataset you want to train your model on.
        :param model_name: The name of your trained model
        :param model_type: The type of model to train.
        :param learning_rate: The learning rate used for training.
        :param num_epochs: Number of epochs for training
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def list(self) -> List[CustomBaseModelResponse]:
        pass

    @abstractmethod
    def get(self, resource_id: str) -> CustomBaseModelResponse:
        pass

    def _create_body(
        self,
        dataset_id: str,
        model_name: str,
        model_type: str,
        learning_rate: Optional[float],
        num_epochs: Optional[int],
        **kwargs,
    ) -> Dict[str, Any]:
        return {
            "dataset_id": dataset_id,
            "model_name": model_name,
            "model_type": model_type,
            "learning_rate": learning_rate,
            "num_epochs": num_epochs,
            **kwargs,
        }
