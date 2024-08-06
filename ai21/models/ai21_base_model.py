import warnings
from typing import Any, Dict

from pydantic import BaseModel, ConfigDict
from typing_extensions import Self

from ai21.models._pydantic_compatibility import _to_dict, _to_json, _from_dict, _from_json, IS_PYDANTIC_V2


class AI21BaseModel(BaseModel):
    if IS_PYDANTIC_V2:
        model_config = ConfigDict(
            populate_by_name=True,
            protected_namespaces=(),
            extra="allow",
        )
    else:

        class Config:
            from pydantic import Extra

            allow_population_by_field_name = True
            extra = Extra.allow

    def to_dict(self, **kwargs) -> Dict[str, Any]:
        warnings.warn(
            "The 'to_dict' method is deprecated and will be removed in a future version."
            " Please use Pydantic's built-in methods instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        kwargs["by_alias"] = kwargs.pop("by_alias", True)

        return _to_dict(self, **kwargs)

    def to_json(self, **kwargs) -> str:
        warnings.warn(
            "The 'to_json' method is deprecated and will be removed in a future version."
            " Please use Pydantic's built-in methods instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        kwargs["by_alias"] = kwargs.pop("by_alias", True)

        return _to_json(self, **kwargs)

    @classmethod
    def from_dict(cls, obj: Any, **kwargs) -> Self:
        warnings.warn(
            "The 'from_dict' method is deprecated and will be removed in a future version."
            " Please use Pydantic's built-in methods instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return _from_dict(cls, obj, **kwargs)

    @classmethod
    def from_json(cls, json_str: str, **kwargs) -> Self:
        warnings.warn(
            "The 'from_json' method is deprecated and will be removed in a future version."
            " Please use Pydantic's built-in methods instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return _from_json(cls, json_str, **kwargs)
