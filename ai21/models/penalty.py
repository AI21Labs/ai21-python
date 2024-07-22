from __future__ import annotations

from typing import Optional

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.pydantic_compatibility import IS_PYDANTIC_V2


class Penalty(AI21BaseModel):
    scale: float
    apply_to_whitespaces: Optional[bool] = None
    apply_to_punctuation: Optional[bool] = None
    apply_to_numbers: Optional[bool] = None
    apply_to_stopwords: Optional[bool] = None
    apply_to_emojis: Optional[bool] = None

    def to_dict(self, **kwargs):
        by_alias = kwargs.pop("by_alias", True)
        exclude_none = kwargs.pop("exclude_none", True)
        if IS_PYDANTIC_V2:
            return super().model_dump(by_alias=by_alias, exclude_none=exclude_none, **kwargs)

        return super().dict(by_alias=by_alias, exclude_none=exclude_none, **kwargs)

    def to_json(self, **kwargs) -> str:
        by_alias = kwargs.pop("by_alias", True)
        exclude_none = kwargs.pop("exclude_none", True)
        if IS_PYDANTIC_V2:
            return super().model_dump_json(by_alias=by_alias, exclude_none=exclude_none, **kwargs)

        return super().json(by_alias=by_alias, exclude_none=exclude_none, **kwargs)
