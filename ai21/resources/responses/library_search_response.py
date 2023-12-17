from dataclasses import dataclass
from typing import Optional, List

from ai21.helpers.camel_case_decorator import camel_case_dataclass_json


@camel_case_dataclass_json
@dataclass
class LibrarySearchResult:
    text: str
    file_id: str
    file_name: str
    score: float
    public_url: Optional[str] = None
    labels: Optional[List[str]] = None


@camel_case_dataclass_json
@dataclass
class LibrarySearchResponse:
    id: str
    results: List[LibrarySearchResult]
