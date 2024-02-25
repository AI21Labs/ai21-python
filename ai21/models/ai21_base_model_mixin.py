from dataclasses_json import LetterCase, DataClassJsonMixin

from ai21.utils.typing import is_not_given


class AI21BaseModelMixin(DataClassJsonMixin):
    dataclass_json_config = {
        "letter_case": LetterCase.CAMEL,
        "exclude": is_not_given,
    }
