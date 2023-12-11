from datetime import datetime

from ai21.models.ai21_base_model import AI21BaseModel


class DatasetResponse(AI21BaseModel):
    id: str
    dataset_name: str
    size_bytes: int
    creation_date: datetime
    num_examples: int
    validation_num_examples: int
    train_num_examples: int
    num_models_used: int
