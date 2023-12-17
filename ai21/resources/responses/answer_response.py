from dataclasses import dataclass
from typing import Optional

from ai21.helpers.camel_case_decorator import camel_case_dataclass_json


@camel_case_dataclass_json
@dataclass
class AnswerResponse:
    id: str
    answer_in_context: Optional[bool]
    answer: Optional[str]
