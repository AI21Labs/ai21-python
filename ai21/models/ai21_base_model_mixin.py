from dataclasses_json import LetterCase, DataClassJsonMixin


class AI21BaseModelMixin(DataClassJsonMixin):
    dataclass_json_config = {
        "letter_case": LetterCase.CAMEL,
    }
