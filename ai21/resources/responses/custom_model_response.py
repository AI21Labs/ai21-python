from dataclasses import dataclass
from typing import Optional

from ai21.helpers.camel_case_decorator import camel_case_dataclass_json


@camel_case_dataclass_json
@dataclass
class ModelMetadata:
    learning_rate: float
    num_epochs: int
    default_epoch: int
    cost: Optional[float] = None
    validation_loss: Optional[float] = None
    eval_loss: Optional[float] = None


@camel_case_dataclass_json
@dataclass
class CustomModelResponse:
    id: str
    name: str
    tier: str
    model_type: str
    custom_model_type: Optional[str]
    status: str
    model_metadata: ModelMetadata
    dataset_id: int
    dataset_name: str
    creation_date: str
    current_epoch: Optional[int]
    size: Optional[str] = None
