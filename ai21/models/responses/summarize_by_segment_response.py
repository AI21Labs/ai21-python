from typing import List, Optional

from pydantic import Field

from ai21.models.ai21_base_model import AI21BaseModel


class Highlight(AI21BaseModel):
    text: str
    start_index: int = Field(alias="startIndex")
    end_index: int = Field(alias="endIndex")


class SegmentSummary(AI21BaseModel):
    summary: Optional[str] = None
    segment_text: Optional[str] = Field(default=None, alias="segmentText")
    segment_html: Optional[str] = Field(default=None, alias="segmentHtml")
    segment_type: str = Field(alias="segmentType")
    has_summary: bool = Field(alias="hasSummary")
    highlights: List[Highlight]


class SummarizeBySegmentResponse(AI21BaseModel):
    id: str
    segments: List[SegmentSummary]
