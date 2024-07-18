from enum import Enum
from typing import List

from ai21.models.ai21_base_model import AI21BaseModel


class CorrectionType(str, Enum):
    GRAMMAR = "Grammar"
    MISSING_WORD = "Missing Word"
    PUNCTUATION = "Punctuation"
    SPELLING = "Spelling"
    WORD_REPETITION = "Word Repetition"
    WRONG_WORD = "Wrong Word"


class Correction(AI21BaseModel):
    suggestion: str
    start_index: int
    end_index: int
    original_text: str
    correction_type: CorrectionType


class GECResponse(AI21BaseModel):
    id: str
    corrections: List[Correction]
