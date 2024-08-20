from typing_extensions import Literal, TypedDict, Required

from ai21.models.chat import FunctionToolDefinition


class ToolDefinition(TypedDict, total=False):
    type: Required[Literal["function"]]
    function: Required[FunctionToolDefinition]
