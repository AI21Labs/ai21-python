import re
from typing import Any, Dict

from pydantic import BaseModel, ConfigDict
from typing_extensions import Self

from ai21.models.pydantic_compatibility import IS_PYDANTIC_V2

if IS_PYDANTIC_V2:
    from pydantic.alias_generators import to_camel


def to_camel_case(snake: str) -> str:
    # Implementation similar to the to_camel of pydantic V2, to be used to support pydantic v1
    if re.match("^[a-z]+[A-Za-z0-9]*$", snake) and not re.search(r"\d[a-z]", snake):
        return snake

    pascal = re.sub("([0-9A-Za-z])_(?=[0-9A-Z])", lambda m: m.group(1), snake.title())
    return re.sub("(^_*[A-Z])", lambda m: m.group(1).lower(), pascal)


class AI21BaseModel(BaseModel):
    if IS_PYDANTIC_V2:
        model_config = ConfigDict(
            alias_generator=to_camel,
            populate_by_name=True,
            protected_namespaces=(),
        )
    else:

        class Config:
            alias_generator = to_camel_case
            allow_population_by_field_name = True

    def to_dict(self, **kwargs) -> Dict[str, Any]:
        by_alias = kwargs.pop("by_alias", True)
        if IS_PYDANTIC_V2:
            return super().model_dump(by_alias=by_alias, **kwargs)

        return super().dict(by_alias=by_alias, **kwargs)

    def to_json(self, **kwargs) -> str:
        by_alias = kwargs.pop("by_alias", True)
        if IS_PYDANTIC_V2:
            return super().model_json(by_alias=by_alias, **kwargs)

        return super().json(by_alias=by_alias, **kwargs)

    @classmethod
    def from_dict(cls, obj: Any, **kwargs) -> Self:
        if IS_PYDANTIC_V2:
            return cls.model_validate(obj, **kwargs)

        return cls.parse_obj(obj, **kwargs)

    @classmethod
    def from_json(cls, json_str: str, **kwargs) -> Self:
        if IS_PYDANTIC_V2:
            return cls.model_validate_json(json_str, **kwargs)

        return cls.parse_raw(json_str, **kwargs)
