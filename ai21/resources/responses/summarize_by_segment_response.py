from dataclasses import dataclass
from typing import List, Optional

from ai21.helpers.camel_case_decorator import camel_case_dataclass_json


@camel_case_dataclass_json
@dataclass
class Highlight:
    text: str
    start_index: int
    end_index: int


@camel_case_dataclass_json
@dataclass
class SegmentSummary:
    summary: Optional[str]
    segment_text: str
    segment_html: Optional[str]
    segment_type: str
    has_summary: bool
    highlights: List[Highlight]


@camel_case_dataclass_json
@dataclass
class SummarizeBySegmentResponse:
    segments: List[SegmentSummary]
