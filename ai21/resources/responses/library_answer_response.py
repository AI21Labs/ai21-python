from dataclasses import dataclass
from typing import List, Optional

from ai21.helpers.camel_case_decorator import camel_case_dataclass_json


@camel_case_dataclass_json
@dataclass
class SourceDocument:
    field_id: str
    name: str
    highlights: List[str]
    public_url: Optional[str] = None


@camel_case_dataclass_json
@dataclass
class LibraryAnswerResponse:
    id: str
    answer_in_context: bool
    answer: Optional[str] = None
    sources: Optional[List[SourceDocument]] = None
