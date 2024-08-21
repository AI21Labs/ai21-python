from typing_extensions import TypedDict, Required

from ai21.models.chat.tool_parameters import ToolParameters


class FunctionToolDefinition(TypedDict, total=False):
    name: Required[str]
    description: str
    parameters: ToolParameters
