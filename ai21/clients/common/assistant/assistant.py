from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from ai21.models.responses.assistant_response import AssistantResponse
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
        optimization: str | NotGiven = NOT_GIVEN,
        avatar: str | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[str] | NotGiven = NOT_GIVEN,
        tool_resources: dict | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> AssistantResponse:
        """
        :param name: The name of the assistant.
        :param description: The description of the assistant.
        :param optimization: The optimization to use.
        :param avatar: The avatar to use.
        :param models: The models to use.
        :param tools: The tools to use.
        :param tool_resources: The tool resources to use.
        :param kwargs: Additional keyword arguments.
        :return: The response object.
        """
        pass

    def _create_body(
        self,
        name: str,
        *,
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
    def list(self) -> List[AssistantResponse]:
        """
        :return: The response object.
        """
        pass

    @abstractmethod
    def get(self, assistant_id: str) -> AssistantResponse:
        """
        :param assistant_id: The ID of the assistant.
        :return: The response object.
        """
        pass

    @abstractmethod
    def modify(
        self,
        assistant_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        optimization: str | NotGiven = NOT_GIVEN,
        avatar: str | NotGiven = NOT_GIVEN,
        is_archived: bool | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[str] | NotGiven = NOT_GIVEN,
        tool_resources: dict | NotGiven = NOT_GIVEN,
    ) -> AssistantResponse:
        """
        :param assistant_id: The ID of the assistant.
        :param name: The name of the assistant.
        :param description: The description of the assistant.
        :param optimization: The optimization to use.
        :param avatar: The avatar to use.
        :param is_archived: Whether the assistant is archived.
        :param models: The models to use.
        :param tools: The tools to use.
        :param tool_resources: The tool resources to use.
        :param kwargs: Additional keyword arguments.
        :return: The response object.
        """
        pass

    def _modify_body(
        self,
        name: str,
        description: str | NotGiven,
        optimization: str | NotGiven,
        avatar: str | NotGiven,
        is_archived: bool | NotGiven,
        models: List[str] | NotGiven,
        tools: List[str] | NotGiven,
        tool_resources: dict | NotGiven,
    ) -> Dict[str, Any]:
        return remove_not_given(
            {
                "name": name,
                "description": description,
                "optimization": optimization,
                "avatar": avatar,
                "is_archived": is_archived,
                "models": models,
                "tools": tools,
                "tool_resources": tool_resources,
            }
        )
