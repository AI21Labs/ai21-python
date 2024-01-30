from dataclasses import dataclass

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class SummarizeResponse(AI21BaseModelMixin):
    id: str
    summary: str
