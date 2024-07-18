from typing import List

from ai21.models.ai21_base_model import AI21BaseModel


class Segment(AI21BaseModel):
    segment_text: str
    segment_type: str


class SegmentationResponse(AI21BaseModel):
    id: str
    segments: List[Segment]
