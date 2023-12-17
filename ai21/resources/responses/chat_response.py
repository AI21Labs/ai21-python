from dataclasses import dataclass
from typing import Optional, List

from ai21.helpers.camel_case_decorator import camel_case_dataclass_json


@camel_case_dataclass_json
@dataclass
class FinishReason:
    reason: str
    length: Optional[int] = None
    sequence: Optional[str] = None


@camel_case_dataclass_json
@dataclass
class ChatOutput:
    text: str
    role: str
    finish_reason: FinishReason


@camel_case_dataclass_json
@dataclass
class ChatResponse:
    outputs: List[ChatOutput]
