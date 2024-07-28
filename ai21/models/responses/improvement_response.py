from typing import List

from pydantic import Field

from ai21.models.ai21_base_model import AI21BaseModel


class Improvement(AI21BaseModel):
    suggestions: List[str]
    start_index: int = Field(alias="startIndex")
    end_index: int = Field(alias="endIndex")
    original_text: str = Field(alias="originalText")
    improvement_type: str = Field(alias="improvementType")


class ImprovementsResponse(AI21BaseModel):
    id: str
    improvements: List[Improvement]
