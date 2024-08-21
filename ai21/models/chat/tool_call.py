from typing import Literal

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.chat.tool_function import ToolFunction


class ToolCall(AI21BaseModel):
    id: str
    function: ToolFunction
    type: Literal["function"] = "function"
