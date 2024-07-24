from typing import List

from pydantic import Field

from ai21.models.ai21_base_model import AI21BaseModel


class Segment(AI21BaseModel):
    segment_text: str = Field(alias="segmentText")
    segment_type: str = Field(alias="segmentType")


class SegmentationResponse(AI21BaseModel):
    id: str
    segments: List[Segment]
