from dataclasses import dataclass
from typing import List

from ai21.helpers.camel_case_decorator import camel_case_dataclass_json


@camel_case_dataclass_json
@dataclass
class Correction:
    suggestion: str
    start_index: int
    end_index: int
    original_text: str
    correction_type: str


@camel_case_dataclass_json
@dataclass
class GECResponse:
    id: str
    corrections: List[Correction]
