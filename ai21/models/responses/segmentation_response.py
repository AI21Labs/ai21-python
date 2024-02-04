from dataclasses import dataclass
from typing import List

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class Segment(AI21BaseModelMixin):
    segment_text: str
    segment_type: str


@dataclass
class SegmentationResponse(AI21BaseModelMixin):
    id: str
    segments: List[Segment]
