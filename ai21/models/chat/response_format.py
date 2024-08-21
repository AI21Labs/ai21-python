from typing import Literal
from typing_extensions import TypedDict, Required


class ResponseFormat(TypedDict, total=False):
    type: Required[Literal["text", "json_object"]]
