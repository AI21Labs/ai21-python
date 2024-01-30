from dataclasses import dataclass
from typing import Optional

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class BaseModelMetadata(AI21BaseModelMixin):
    learning_rate: float
    num_epochs: int
    default_epoch: int
    cost: Optional[float] = None
    validation_loss: Optional[float] = None
    eval_loss: Optional[float] = None


@dataclass
class CustomBaseModelResponse(AI21BaseModelMixin):
    id: str
    name: str
    tier: str
    model_type: str
    custom_model_type: Optional[str]
    status: str
    model_metadata: BaseModelMetadata
    dataset_id: int
    dataset_name: str
    creation_date: str
    current_epoch: Optional[int]
    size: Optional[str] = None
