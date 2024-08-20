from typing import Optional

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.chat.tool_parameters import ToolParameters


class FunctionToolDefinition(AI21BaseModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[ToolParameters] = None
