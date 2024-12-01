from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from ai21.models.assistant.assistant import Optimization, Tool
from ai21.models.responses.assistant_response import (
    Assistant,
    ToolResources,
    ListAssistant,
)
from ai21.types import NotGiven, NOT_GIVEN
from ai21.utils.typing import remove_not_given


class Assistants(ABC):
    _module_name = "assistants"

    @abstractmethod
    def create(
        self,
        name: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        optimization: Optimization | NotGiven = NOT_GIVEN,
        avatar: str | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> Assistant:
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
    def list(self) -> ListAssistant:
        pass

    @abstractmethod
    def get(self, assistant_id: str) -> Assistant:
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
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
    ) -> Assistant:
        pass
