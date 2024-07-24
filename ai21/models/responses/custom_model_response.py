from typing import Optional

from pydantic import Field

from ai21.models.ai21_base_model import AI21BaseModel


class BaseModelMetadata(AI21BaseModel):
    learning_rate: float = Field(alias="learningRate")
    num_epochs: int = Field(alias="numEpochs")
    default_epoch: int = Field(alias="defaultEpoch")
    cost: Optional[float] = None
    validation_loss: Optional[float] = Field(None, alias="validationLoss")
    eval_loss: Optional[float] = Field(None, alias="evalLoss")


class CustomBaseModelResponse(AI21BaseModel):
    id: str
    name: str
    tier: str
    model_type: str = Field(alias="modelType")
    custom_model_type: Optional[str] = Field(alias="customModelType")
    status: str
    model_metadata: BaseModelMetadata = Field(alias="modelMetadata")
    dataset_id: int = Field(alias="datasetId")
    dataset_name: str = Field(alias="datasetName")
    creation_date: str = Field(alias="creationDate")
    current_epoch: Optional[int] = Field(alias="currentEpoch")
    size: Optional[str] = None
