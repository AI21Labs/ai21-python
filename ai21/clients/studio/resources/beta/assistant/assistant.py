from __future__ import annotations

from typing import List

from ai21.clients.common.beta.assistant.assistants import Assistants
from ai21.clients.studio.resources.studio_resource import (
    AsyncStudioResource,
    StudioResource,
)
from ai21.models.assistant.assistant import Tool, ToolResources
from ai21.models.responses.assistant_response import AssistantResponse, ListAssistant
from ai21.types import NotGiven, NOT_GIVEN


class Assistant(StudioResource, Assistants):
    def create(
        self,
        name: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        optimization: str | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> AssistantResponse:
        body = self._create_body(
            name=name,
            description=description,
            optimization=optimization,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            **kwargs,
        )

        return self._post(path=f"/{self._module_name}", body=body, response_cls=AssistantResponse)

    def retrieve(self, assistant_id: str) -> AssistantResponse:
        return self._get(path=f"/{self._module_name}/{assistant_id}", response_cls=AssistantResponse)

    def list(self) -> ListAssistant:
        return self._get(path=f"/{self._module_name}", response_cls=ListAssistant)

    def modify(
        self,
        assistant_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        optimization: str | NotGiven = NOT_GIVEN,
        is_archived: bool | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
    ) -> AssistantResponse:
        body = self._create_body(
            name=name,
            description=description,
            optimization=optimization,
            is_archived=is_archived,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
        )

        return self._patch(path=f"/{self._module_name}/{assistant_id}", body=body, response_cls=AssistantResponse)


class AsyncAssistant(AsyncStudioResource, Assistants):
    async def create(
        self,
        name: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        optimization: str | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> AssistantResponse:
        body = self._create_body(
            name=name,
            description=description,
            optimization=optimization,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            **kwargs,
        )

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=AssistantResponse)

    async def retrieve(self, assistant_id: str) -> AssistantResponse:
        return await self._get(path=f"/{self._module_name}/{assistant_id}", response_cls=AssistantResponse)

    async def list(self) -> ListAssistant:
        return await self._get(path=f"/{self._module_name}", response_cls=ListAssistant)

    async def modify(
        self,
        assistant_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        optimization: str | NotGiven = NOT_GIVEN,
        is_archived: bool | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
    ) -> AssistantResponse:
        body = self._create_body(
            name=name,
            description=description,
            optimization=optimization,
            is_archived=is_archived,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
        )

        return await self._patch(path=f"/{self._module_name}/{assistant_id}", body=body, response_cls=AssistantResponse)
