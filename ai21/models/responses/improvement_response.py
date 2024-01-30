from dataclasses import dataclass
from typing import List

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class Improvement(AI21BaseModelMixin):
    suggestions: List[str]
    start_index: int
    end_index: int
    original_text: str
    improvement_type: str


@dataclass
class ImprovementsResponse(AI21BaseModelMixin):
    id: str
    improvements: List[Improvement]
