from dataclasses import dataclass
from typing import Optional

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class Penalty(AI21BaseModelMixin):
    scale: float
    apply_to_whitespaces: Optional[bool] = None
    apply_to_punctuation: Optional[bool] = None
    apply_to_numbers: Optional[bool] = None
    apply_to_stopwords: Optional[bool] = None
    apply_to_emojis: Optional[bool] = None
