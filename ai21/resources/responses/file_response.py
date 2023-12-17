from dataclasses import dataclass
from datetime import date
from typing import Optional, List

from ai21.helpers.camel_case_decorator import camel_case_dataclass_json


@camel_case_dataclass_json
@dataclass
class FileResponse:
    file_id: str
    name: str
    file_type: str
    size_bytes: int
    created_by: str
    creation_date: date
    last_updated: date
    status: str
    path: Optional[str] = None
    labels: Optional[List[str]] = None
    public_url: Optional[str] = None
    error_code: Optional[int] = None
    error_message: Optional[str] = None
