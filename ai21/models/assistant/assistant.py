from typing import Optional, Literal

from typing_extensions import TypedDict

Optimization = Literal["cost", "latency"]
Tool = Literal["rag", "web_search", "plan_approval"]


class ToolResources(TypedDict, total=False):
    rag: Optional[dict]
    web_search: Optional[dict]
    plan_approval: Optional[dict]
