from dataclasses import dataclass
from typing import List

from ai21.helpers.camel_case_decorator import camel_case_dataclass_json


@camel_case_dataclass_json
@dataclass
class EmbedResult:
    embedding: List[float]


@camel_case_dataclass_json
@dataclass
class EmbedResponse:
    id: str
    results: List[EmbedResult]
