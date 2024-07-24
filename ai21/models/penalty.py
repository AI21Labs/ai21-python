from __future__ import annotations

from typing import Optional

from ai21.models.ai21_base_model import AI21BaseModel
from pydantic import Field


class Penalty(AI21BaseModel):
    scale: float
    apply_to_whitespaces: Optional[bool] = Field(default=None, alias="applyToWhitespaces")
    apply_to_punctuation: Optional[bool] = Field(default=None, alias="applyToPunctuation")
    apply_to_numbers: Optional[bool] = Field(default=None, alias="applyToNumbers")
    apply_to_stopwords: Optional[bool] = Field(default=None, alias="applyToStopwords")
    apply_to_emojis: Optional[bool] = Field(default=None, alias="applyToEmojis")

    def to_dict(self, **kwargs):
        kwargs["by_alias"] = kwargs.pop("by_alias", True)
        kwargs["exclude_none"] = kwargs.pop("exclude_none", True)

        return super().to_dict(**kwargs)

    def to_json(self, **kwargs) -> str:
        kwargs["by_alias"] = kwargs.pop("by_alias", True)
        kwargs["exclude_none"] = kwargs.pop("exclude_none", True)

        return super().to_json(**kwargs)
