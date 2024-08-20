from typing_extensions import Literal, Any, Dict, List, TypedDict, Required


class ToolParameters(TypedDict, total=False):
    type: Literal["object"]
    properties: Required[Dict[str, Any]]
    required: List[str]
