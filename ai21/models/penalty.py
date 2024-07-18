from __future__ import annotations

from typing import Optional

from ai21.models.ai21_base_model import AI21BaseModel


class Penalty(AI21BaseModel):
    scale: float
    apply_to_whitespaces: Optional[bool] = None
    apply_to_punctuation: Optional[bool] = None
    apply_to_numbers: Optional[bool] = None
    apply_to_stopwords: Optional[bool] = None
    apply_to_emojis: Optional[bool] = None

    def to_dict(self):
        return super().dict(by_alias=True, exclude_none=True)
