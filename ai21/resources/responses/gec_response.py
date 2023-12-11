from typing import List

from ai21.models.ai21_base_model import AI21BaseModel


class Correction(AI21BaseModel):
    suggestion: str
    start_index: int
    end_index: int
    original_text: str
    correction_type: str


class GECResponse(AI21BaseModel):
    id: str
    corrections: List[Correction]
