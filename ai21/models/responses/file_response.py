from datetime import date
from typing import Optional, List

from pydantic import Field

from ai21.models.ai21_base_model import AI21BaseModel


class FileResponse(AI21BaseModel):
    file_id: str = Field(alias="fileId")
    name: str
    file_type: str = Field(alias="fileType")
    size_bytes: int = Field(alias="sizeBytes")
    created_by: str = Field(alias="createdBy")
    creation_date: date = Field(alias="creationDate")
    last_updated: date = Field(alias="lastUpdated")
    status: str
    path: Optional[str] = None
    labels: Optional[List[str]] = None
    public_url: Optional[str] = Field(default=None, alias="publicUrl")
    error_code: Optional[int] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
