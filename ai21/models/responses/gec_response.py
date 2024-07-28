from enum import Enum
from typing import List

from pydantic import Field

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
    start_index: int = Field(alias="startIndex")
    end_index: int = Field(alias="endIndex")
    original_text: str = Field(alias="originalText")
    correction_type: CorrectionType = Field(alias="correctionType")


class GECResponse(AI21BaseModel):
    id: str
    corrections: List[Correction]
