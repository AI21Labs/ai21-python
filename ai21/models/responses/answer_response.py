from dataclasses import dataclass
from typing import Optional

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class AnswerResponse(AI21BaseModelMixin):
    id: str
    answer_in_context: Optional[bool] = None
    answer: Optional[str] = None
