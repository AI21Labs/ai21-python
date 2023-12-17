from abc import ABC

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from dataclasses_json import dataclass_json, LetterCase, DataClassJsonMixin


class AI21BaseModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, protected_namespaces=())


class AI21ModelMixin(DataClassJsonMixin):
    letter_case = LetterCase.CAMEL
