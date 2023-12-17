from dataclasses import dataclass
from typing import List

from ai21.helpers.camel_case_decorator import camel_case_dataclass_json


@camel_case_dataclass_json
@dataclass
class Segment:
    segment_text: str
    segment_type: str


@camel_case_dataclass_json
@dataclass
class SegmentationResponse:
    segments: List[Segment]
