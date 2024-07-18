from typing import List, Optional

from ai21.models.ai21_base_model import AI21BaseModel


class Highlight(AI21BaseModel):
    text: str
    start_index: int
    end_index: int


class SegmentSummary(AI21BaseModel):
    summary: Optional[str]
    segment_text: str
    segment_html: Optional[str]
    segment_type: str
    has_summary: bool
    highlights: List[Highlight]


class SummarizeBySegmentResponse(AI21BaseModel):
    id: str
    segments: List[SegmentSummary]
