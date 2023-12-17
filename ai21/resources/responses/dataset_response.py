from dataclasses import dataclass
from datetime import datetime

from ai21.helpers.camel_case_decorator import camel_case_dataclass_json


@camel_case_dataclass_json
@dataclass
class DatasetResponse:
    id: str
    dataset_name: str
    size_bytes: int
    creation_date: datetime
    num_examples: int
    validation_num_examples: int
    train_num_examples: int
    num_models_used: int
