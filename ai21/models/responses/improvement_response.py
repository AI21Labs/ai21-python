from typing import List

from ai21.models.ai21_base_model import AI21BaseModel


class Improvement(AI21BaseModel):
    suggestions: List[str]
    start_index: int
    end_index: int
    original_text: str
    improvement_type: str


class ImprovementsResponse(AI21BaseModel):
    id: str
    improvements: List[Improvement]
