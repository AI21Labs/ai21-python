from dataclasses import dataclass
from typing import List

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class EmbedResult(AI21BaseModelMixin):
    embedding: List[float]


@dataclass
class EmbedResponse(AI21BaseModelMixin):
    id: str
    results: List[EmbedResult]
