from dataclasses import dataclass

from ai21.helpers.camel_case_decorator import camel_case_dataclass_json


@camel_case_dataclass_json
@dataclass
class SummarizeResponse:
    id: str
    summary: str
