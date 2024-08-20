from typing_extensions import Literal, Any, Dict, List, TypedDict, Required


class ToolParameters(TypedDict, total=False):
    properties: Required[Dict[str, Any]]
    type: Literal["object"]
    required: List[str]
