from typing import Dict, Literal, Any, List, Set, Optional

from typing_extensions import TypedDict


RunStatus = Literal[
    "cancelled",
    "cancelling",
    "completed",
    "expired",
    "failed",
    "incomplete",
    "in_progress",
    "queued",
    "requires_action",
]

TERMINATED_RUN_STATUSES: Set[RunStatus] = {"completed", "failed", "expired", "cancelled", "requires_action"}
DEFAULT_RUN_POLL_INTERVAL: float = 1  # seconds
DEFAULT_RUN_POLL_TIMEOUT: float = 60  # seconds


class ToolOutput(TypedDict):
    tool_call_id: str
    output: Any


class Function(TypedDict):
    name: str
    arguments: Any


class ToolCall(TypedDict):
    type: Literal["function"]
    id: str
    function: Function


class SubmitToolCallOutputs(TypedDict):
    tool_calls: List[ToolOutput]


class SubmitInput(TypedDict):
    event_name: str
    data: Dict[str, Any]


class RequiredAction(TypedDict, total=False):
    type: Literal["submit_tool_outputs", "submit_input"]
    submit_tool_outputs: Optional[SubmitToolCallOutputs] = None
    submit_input: Optional[SubmitInput] = None
