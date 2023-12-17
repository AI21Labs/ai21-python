from dataclasses_json import dataclass_json, LetterCase


def camel_case_dataclass_json(cls):
    return dataclass_json(letter_case=LetterCase.CAMEL)(cls)
