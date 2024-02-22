from __future__ import annotations

from dataclasses import dataclass

from ai21.types import NOT_GIVEN, NotGiven
from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class Penalty(AI21BaseModelMixin):
    scale: float
    apply_to_whitespaces: bool | NotGiven = NOT_GIVEN
    apply_to_punctuation: bool | NotGiven = NOT_GIVEN
    apply_to_numbers: bool | NotGiven = NOT_GIVEN
    apply_to_stopwords: bool | NotGiven = NOT_GIVEN
    apply_to_emojis: bool | NotGiven = NOT_GIVEN
