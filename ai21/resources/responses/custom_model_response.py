from typing import Optional

from ai21.models.ai21_base_model import AI21BaseModel


class ModelMetadata(AI21BaseModel):
    learning_rate: float
    cost: Optional[float] = None
    validation_loss: Optional[float] = None
    eval_loss: Optional[float] = None
    num_epochs: int
    default_epoch: int


class CustomModelResponse(AI21BaseModel):
    id: str
    name: str
    tier: str
    size: Optional[str] = None
    model_type: str
    custom_model_type: Optional[str]
    status: str
    model_metadata: ModelMetadata
    dataset_id: int
    dataset_name: str
    creation_date: str
    current_epoch: Optional[int]
