from typing_extensions import Literal, List, Optional, Union, TypeAlias

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.chat.tool_call import ToolCall


class ChatMessage(AI21BaseModel):
    role: str
    content: str


class AssistantMessage(ChatMessage):
    role: Literal["assistant"] = "assistant"
    tool_calls: Optional[List[ToolCall]] = None
    content: Optional[str] = None


class ToolMessage(ChatMessage):
    role: Literal["tool"] = "tool"
    tool_call_id: str


class UserMessage(ChatMessage):
    role: Literal["user"] = "user"


class SystemMessage(ChatMessage):
    role: Literal["system"] = "system"


ChatMessageParam: TypeAlias = Union[UserMessage, AssistantMessage, ToolMessage, SystemMessage, ChatMessage]
