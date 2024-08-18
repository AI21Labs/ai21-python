from typing import Literal

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.chat.function_tool_definition import FunctionToolDefinition


class ToolDefinition(AI21BaseModel):
    type: Literal["function"]
    function: FunctionToolDefinition
