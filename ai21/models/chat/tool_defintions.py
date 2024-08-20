from typing_extensions import Literal, TypedDict

from ai21.models.chat import FunctionToolDefinition


class ToolDefinition(TypedDict, total=False):
    type: Literal["function"]
    function: FunctionToolDefinition
