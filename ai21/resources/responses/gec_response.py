from dataclasses import dataclass
from typing import List

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class Correction(AI21BaseModelMixin):
    suggestion: str
    start_index: int
    end_index: int
    original_text: str
    correction_type: str


@dataclass
class GECResponse(AI21BaseModelMixin):
    id: str
    corrections: List[Correction]
