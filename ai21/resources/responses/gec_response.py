from dataclasses import dataclass
from enum import Enum
from typing import List

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


class CorrectionType(str, Enum):
    GRAMMAR = "Grammar"
    MISSING_WORD = "Missing Word"
    PUNCTUATION = "Punctuation"
    SPELLING = "Spelling"
    WORD_REPETITION = "Word Repetition"
    WRONG_WORD = "Wrong Word"


@dataclass
class Correction(AI21BaseModelMixin):
    suggestion: str
    start_index: int
    end_index: int
    original_text: str
    correction_type: CorrectionType


@dataclass
class GECResponse(AI21BaseModelMixin):
    id: str
    corrections: List[Correction]
