from typing import TypedDict, Literal, List, Optional, Any, Set

from ai21.models.ai21_base_model import AI21BaseModel

Budget = Literal["low", "medium", "high"]
Role = Literal["user", "assistant"]
RunStatus = Literal["completed", "failed", "in_progress", "requires_action"]
ToolType = Literal["file_search", "web_search"]

DEFAULT_RUN_POLL_INTERVAL: float = 1  # seconds
DEFAULT_RUN_POLL_TIMEOUT: float = 120  # seconds
TERMINATED_RUN_STATUSES: Set[RunStatus] = {"completed", "failed", "requires_action"}


class Tool(TypedDict):
    type: ToolType


class FileSearchToolResource(TypedDict, total=False):
    retrieval_similarity_threshold: Optional[float]
    labels: Optional[List[str]]
    labels_filter_mode: Optional[Literal["AND", "OR"]]
    labels_filter: Optional[dict]
    file_ids: Optional[List[str]]
    retrieval_strategy: Optional[str]
    max_neighbors: Optional[int]


class WebSearchToolResource(TypedDict, total=False):
    urls: Optional[List[str]]
    fallback_to_web: Optional[bool]


class ToolResources(TypedDict):
    file_search: FileSearchToolResource
    web_search: WebSearchToolResource


class Constraint(TypedDict):
    name: str
    description: str
    is_mandatory: bool


class RunResponse(AI21BaseModel):
    id: str
    status: RunStatus
    result: Any
