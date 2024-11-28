from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from ai21.models.responses.assistant_response import (
    AssistantResponse,
    Optimization,
    ToolResources,
    Model,
    Tool,
    ListAssistantResponse,
)
from ai21.types import NotGiven, NOT_GIVEN
from ai21.utils.typing import remove_not_given


class Assistant(ABC):
    _module_name = "assistants"

    @abstractmethod
    def create(
        self,
        name: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        optimization: Optimization | NotGiven = NOT_GIVEN,
        avatar: str | NotGiven = NOT_GIVEN,
        models: List[Model] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> AssistantResponse:
        pass

    def _create_body(
        self,
        *,
        name: str,
        description: str | NotGiven,
        optimization: str | NotGiven,
        avatar: str | NotGiven,
        models: List[str] | NotGiven,
        tools: List[str] | NotGiven,
        tool_resources: dict | NotGiven,
        **kwargs,
    ) -> Dict[str, Any]:
        return remove_not_given(
            {
                "name": name,
                "description": description,
                "optimization": optimization,
                "avatar": avatar,
                "models": models,
                "tools": tools,
                "tool_resources": tool_resources,
                **kwargs,
            }
        )

    @abstractmethod
    def list(self) -> ListAssistantResponse:
        pass

    @abstractmethod
    def get(self, assistant_id: str) -> AssistantResponse:
        pass

    @abstractmethod
    def modify(
        self,
        assistant_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        optimization: Optimization | NotGiven = NOT_GIVEN,
        avatar: str | NotGiven = NOT_GIVEN,
        is_archived: bool | NotGiven = NOT_GIVEN,
        models: List[Model] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
    ) -> AssistantResponse:
        pass
