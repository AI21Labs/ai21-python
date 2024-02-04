from dataclasses import dataclass
from typing import List

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class Suggestion(AI21BaseModelMixin):
    text: str


@dataclass
class ParaphraseResponse(AI21BaseModelMixin):
    id: str
    suggestions: List[Suggestion]
