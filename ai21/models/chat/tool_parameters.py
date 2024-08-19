from typing import Literal, Any, Dict, List, Optional
from ai21.models.ai21_base_model import AI21BaseModel


class ToolParameters(AI21BaseModel):
    properties: Dict[str, Any]
    type: Literal["object"] = "object"
    required: Optional[List[str]] = None
