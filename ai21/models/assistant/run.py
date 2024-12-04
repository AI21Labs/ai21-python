from typing import Literal, Any, List

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


class RequiredAction(TypedDict):
    type: Literal["submit_tool_outputs"]
    submit_tool_outputs: SubmitToolCallOutputs
