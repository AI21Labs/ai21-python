import uuid
from datetime import date
from typing import Optional

from ai21.models.ai21_base_model import AI21BaseModel


class FileResponse(AI21BaseModel):
    file_id: str
    name: str
    file_type: str
    size_bytes: int
    created_by: str
    creation_date: date
    last_updated: date
    status: str
    path: Optional[str] = None
    labels: Optional[list[str]] = None
    public_url: Optional[str] = None
    error_code: Optional[int] = None
    error_message: Optional[str] = None
