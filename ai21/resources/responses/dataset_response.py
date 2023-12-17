from dataclasses import dataclass
from datetime import datetime

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class DatasetResponse(AI21BaseModelMixin):
    id: str
    dataset_name: str
    size_bytes: int
    creation_date: datetime
    num_examples: int
    validation_num_examples: int
    train_num_examples: int
    num_models_used: int
