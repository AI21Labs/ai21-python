from dataclasses import dataclass
from typing import List, Optional

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class Highlight(AI21BaseModelMixin):
    text: str
    start_index: int
    end_index: int


@dataclass
class SegmentSummary(AI21BaseModelMixin):
    summary: Optional[str]
    segment_text: str
    segment_html: Optional[str]
    segment_type: str
    has_summary: bool
    highlights: List[Highlight]


@dataclass
class SummarizeBySegmentResponse(AI21BaseModelMixin):
    id: str
    segments: List[SegmentSummary]
