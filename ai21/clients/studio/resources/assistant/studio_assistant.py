from __future__ import annotations

from typing import List

from ai21.clients.common.assistant.assistant import Assistant
from ai21.clients.studio.resources.studio_resource import (
    AsyncStudioResource,
    StudioResource,
)
from ai21.models.responses.assistant_response import (
    AssistantResponse,
    Tool,
    ToolResources,
    ListAssistantResponse,
)
from ai21.types import NotGiven, NOT_GIVEN


class StudioAssistant(StudioResource, Assistant):
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
    ) -> AssistantResponse:
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

        return self._post(path=f"/{self._module_name}", body=body, response_cls=AssistantResponse)

    def get(self, assistant_id: str) -> AssistantResponse:
        return self._get(path=f"/{self._module_name}/{assistant_id}", response_cls=AssistantResponse)

    def list(self) -> ListAssistantResponse:
        return self._get(path=f"/{self._module_name}", response_cls=ListAssistantResponse)

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
    ) -> AssistantResponse:
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

        return self._patch(path=f"/{self._module_name}/{assistant_id}", body=body, response_cls=AssistantResponse)


class AsyncStudioAssistant(AsyncStudioResource, Assistant):
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
    ) -> AssistantResponse:
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

        return self._post(path=f"/{self._module_name}", body=body, response_cls=AssistantResponse)

    async def get(self, assistant_id: str) -> AssistantResponse:
        return await self._get(path=f"/{self._module_name}/{assistant_id}", response_cls=AssistantResponse)

    async def list(self) -> ListAssistantResponse:
        return await self._get(path=f"/{self._module_name}", response_cls=ListAssistantResponse)

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
    ) -> AssistantResponse:
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

        return await self._patch(path=f"/{self._module_name}/{assistant_id}", body=body, response_cls=AssistantResponse)
