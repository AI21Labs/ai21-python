from typing import Literal, List, Optional, Any, Set, Dict, Type, Union
from typing_extensions import TypedDict, Required, Annotated
from pydantic import BaseModel, Field

from ai21.models.ai21_base_model import AI21BaseModel

Budget = Literal["low", "medium", "high"]
Role = Literal["user", "assistant"]
RunStatus = Literal["completed", "failed", "in_progress", "requires_action"]
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


class HTTPToolFunctionParamProperties(TypedDict):
    type: str
    description: str


class Parameters(TypedDict, total=False):
    type: Literal["object"]
    properties: Dict[str, HTTPToolFunctionParamProperties]
    required: List[str]
    additional_properties: Optional[bool]


class Function(TypedDict):
    name: str
    description: str
    parameters: Parameters


class Endpoint(TypedDict, total=False):
    url: str
    headers: Optional[dict]


class HttpTool(TypedDict):
    type: Required[Literal["http"]]
    function: Function
    endpoint: Endpoint


class McpTool(TypedDict, total=False):
    type: Required[Literal["mcp"]]
    server_label: str
    server_url: str
    headers: Optional[dict]
    allowed_tools: Optional[List[str]]


class FileSearch(TypedDict, total=False):
    type: Literal["file_search"]
    retrieval_similarity_threshold: Optional[float]
    labels: Optional[List[str]]
    labels_filter_mode: Optional[Literal["AND", "OR"]]
    labels_filter: Optional[dict]
    file_ids: Optional[List[str]]
    retrieval_strategy: Optional[str]
    max_neighbors: Optional[int]


class WebSearch(TypedDict, total=False):
    type: Literal["web_search"]
    urls: Optional[List[str]]
    query_suffix: Optional[str]
    rephrase_query: Optional[bool]
    use_cached_pages: Optional[bool]


class ToolResources(TypedDict, total=False):
    file_search: Optional[FileSearch]
    web_search: Optional[WebSearch]


ToolDefinition = Annotated[
    Union[
        HttpTool,
        McpTool,
        FileSearch,
        WebSearch,
    ],
    Field(discriminator="type"),
]


class Requirement(TypedDict, total=False):
    name: str
    description: str
    is_mandatory: bool


class RequirementResultItem(Requirement, total=False):
    score: float
    reason: Optional[str]


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


class ToolCallResult(TypedDict, total=False):
    tool_name: str
    tool_type: Literal["mcp", "http"]
    server_label: Optional[str]
    parameters: Dict[str, Any]
    response: Dict[str, Any]
    status: Literal["success", "failure"]


class DataSources(TypedDict, total=False):
    file_search: Optional[List[FileSearchResult]]
    web_search: Optional[List[WebSearchResult]]
    tool_calls: Optional[List[ToolCallResult]]


class RunError(TypedDict):
    message: str


class RunResponse(AI21BaseModel):
    id: str
    status: RunStatus
    result: Any
    data_sources: Optional[DataSources] = None
    requirements_result: Optional[RequirementsResult] = None
    error: Optional[RunError] = None
