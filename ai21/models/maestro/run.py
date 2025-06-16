from typing import Literal, List, Optional, Any, Set, Dict, Type, Union
from typing_extensions import TypedDict
from pydantic import BaseModel

from ai21.models.ai21_base_model import AI21BaseModel

Budget = Literal["low", "medium", "high"]
Role = Literal["user", "assistant"]
RunStatus = Literal["completed", "failed", "in_progress", "requires_action"]
ToolType = Literal["file_search", "web_search"]
OutputOptions = Literal["data_sources", "requirements_result"]
PrimitiveTypes = Union[Type[str], Type[int], Type[float], Type[bool]]
PrimitiveLists = Type[List[PrimitiveTypes]]
OutputType = Union[Type[BaseModel], PrimitiveTypes, Dict[str, Any]]

DEFAULT_RUN_POLL_INTERVAL: float = 1  # seconds
DEFAULT_RUN_POLL_TIMEOUT: float = 120  # seconds
TERMINATED_RUN_STATUSES: Set[RunStatus] = {"completed", "failed", "requires_action"}


class MaestroMessage(TypedDict):
    role: Role
    content: str


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


class ToolResources(TypedDict, total=False):
    file_search: Optional[FileSearchToolResource]
    web_search: Optional[WebSearchToolResource]


class Requirement(TypedDict, total=False):
    name: str
    description: str
    is_mandatory: bool = False


class RequirementResultItem(Requirement, total=False):
    score: float
    reason: Optional[str] = None


class RequirementsResult(TypedDict, total=False):
    score: float
    finish_reason: str
    requirements: List[RequirementResultItem]


class FileSearchResult(TypedDict, total=False):
    text: Optional[str]
    file_id: str
    file_name: str
    score: float
    order: int


class WebSearchResult(TypedDict, total=False):
    text: str
    url: str
    score: float


class DataSources(TypedDict, total=False):
    file_search: Optional[List[FileSearchResult]]
    web_search: Optional[List[WebSearchResult]]


class RunResponse(AI21BaseModel):
    id: str
    status: RunStatus
    result: Any
    data_sources: Optional[DataSources] = None
    requirements_result: Optional[RequirementsResult] = None
