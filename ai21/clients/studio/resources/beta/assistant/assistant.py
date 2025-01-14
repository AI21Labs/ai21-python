from __future__ import annotations

from typing import List

from ai21.clients.common.beta.assistant.assistants import BaseAssistants
from ai21.clients.studio.resources.beta.assistant.assistants_plans import AssistantPlans, AsyncAssistantPlans
from ai21.clients.studio.resources.beta.assistant.assistant_routes import AssistantRoutes, AsyncAssistantRoutes
from ai21.clients.studio.resources.studio_resource import (
    AsyncStudioResource,
    StudioResource,
)
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models.assistant.assistant import Tool, ToolResources
from ai21.models.responses.assistant_response import AssistantResponse, ListAssistant, DeletedAssistantResponse
from ai21.types import NotGiven, NOT_GIVEN


class Assistants(StudioResource, BaseAssistants):
    def __init__(self, client: AI21HTTPClient):
        super().__init__(client)

        self.plans = AssistantPlans(client)
        self.routes = AssistantRoutes(client)

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

    def delete(self, assistant_id: str) -> DeletedAssistantResponse:
        return self._delete(path=f"/{self._module_name}/{assistant_id}", response_cls=DeletedAssistantResponse)


class AsyncAssistants(AsyncStudioResource, BaseAssistants):
    def __init__(self, client: AsyncAI21HTTPClient):
        super().__init__(client)

        self.plans = AsyncAssistantPlans(client)
        self.routes = AsyncAssistantRoutes(client)

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

    async def delete(self, assistant_id: str) -> DeletedAssistantResponse:
        return await self._delete(path=f"/{self._module_name}/{assistant_id}", response_cls=DeletedAssistantResponse)
