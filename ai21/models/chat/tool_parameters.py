from __future__ import annotations
from typing import Literal, Any, Dict, List
from pydantic import Field
from ai21.models.ai21_base_model import AI21BaseModel


class ToolParameters(AI21BaseModel):
    properties: Dict[str, Any]
    type: Literal["object"] = Field(
        default="object",
        description="Type of the parameter schema, only `object` is supported",
    )
    required: List[str] | None = Field(None, description="List of required properties")
