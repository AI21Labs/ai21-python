from datetime import datetime

from pydantic import Field

from ai21.models.ai21_base_model import AI21BaseModel


class DatasetResponse(AI21BaseModel):
    id: str
    dataset_name: str = Field(alias="datasetName")
    size_bytes: int = Field(alias="sizeBytes")
    creation_date: datetime = Field(alias="creationDate")
    num_examples: int = Field(alias="numExamples")
    validation_num_examples: int = Field(alias="validationNumExamples")
    train_num_examples: int = Field(alias="trainNumExamples")
    num_models_used: int = Field(alias="numModelsUsed")
