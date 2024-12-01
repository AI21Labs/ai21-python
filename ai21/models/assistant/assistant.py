from typing import Optional, Literal

from typing_extensions import TypedDict

Optimization = Literal["cost", "latency"]
Tool = Literal["rag", "internet_research", "plan_approval"]


class ToolResources(TypedDict, total=False):
    rag: Optional[dict]
    internet_research: Optional[dict]
    plan_approval: Optional[dict]
