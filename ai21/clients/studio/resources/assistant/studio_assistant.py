from __future__ import annotations

from typing import List

from ai21.clients.common.assistant.assistants import Assistants
from ai21.clients.studio.resources.studio_resource import (
    AsyncStudioResource,
    StudioResource,
)
from ai21.models.assistant.assistant import Tool, ToolResources
from ai21.models.responses.assistant_response import Assistant, ListAssistant
from ai21.types import NotGiven, NOT_GIVEN


class StudioAssistant(StudioResource, Assistants):
    def create(
        self,
        name: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        optimization: str | NotGiven = NOT_GIVEN,
        avatar: str | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> Assistant:
        body = self._create_body(
            name=name,
            description=description,
            optimization=optimization,
            avatar=avatar,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            **kwargs,
        )

        return self._post(path=f"/{self._module_name}", body=body, response_cls=Assistant)

    def get(self, assistant_id: str) -> Assistant:
        return self._get(path=f"/{self._module_name}/{assistant_id}", response_cls=Assistant)

    def list(self) -> ListAssistant:
        return self._get(path=f"/{self._module_name}", response_cls=ListAssistant)

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
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
    ) -> Assistant:
        body = self._create_body(
            name=name,
            description=description,
            optimization=optimization,
            avatar=avatar,
            is_archived=is_archived,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
        )

        return self._patch(path=f"/{self._module_name}/{assistant_id}", body=body, response_cls=Assistant)


class AsyncStudioAssistant(AsyncStudioResource, Assistants):
    async def create(
        self,
        name: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        optimization: str | NotGiven = NOT_GIVEN,
        avatar: str | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> Assistant:
        body = self._create_body(
            name=name,
            description=description,
            optimization=optimization,
            avatar=avatar,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            **kwargs,
        )

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=Assistant)

    async def get(self, assistant_id: str) -> Assistant:
        return await self._get(path=f"/{self._module_name}/{assistant_id}", response_cls=Assistant)

    async def list(self) -> ListAssistant:
        return await self._get(path=f"/{self._module_name}", response_cls=ListAssistant)

    async def modify(
        self,
        assistant_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        optimization: str | NotGiven = NOT_GIVEN,
        avatar: str | NotGiven = NOT_GIVEN,
        is_archived: bool | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
    ) -> Assistant:
        body = self._create_body(
            name=name,
            description=description,
            optimization=optimization,
            avatar=avatar,
            is_archived=is_archived,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
        )

        return await self._patch(path=f"/{self._module_name}/{assistant_id}", body=body, response_cls=Assistant)
