import re
from typing import Any

from pydantic import BaseModel, ConfigDict

from ai21.models.pydantic_compatibility import IS_PYDANTIC_V2

if IS_PYDANTIC_V2:
    from pydantic.alias_generators import to_camel


def to_camel_case(snake: str) -> str:
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

    def to_dict(self):
        return super().dict()

    @classmethod
    def from_dict(cls, obj: Any) -> "AI21BaseModel":
        return cls.parse_obj(obj)
