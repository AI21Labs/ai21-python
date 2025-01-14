from __future__ import annotations

from typing import List

from ai21.clients.common.beta.assistant.routes import BaseRoutes
from ai21.clients.studio.resources.studio_resource import (
    AsyncStudioResource,
    StudioResource,
)
from ai21.models.responses.route_response import RouteResponse, ListRouteResponse
from ai21.types import NotGiven, NOT_GIVEN


class AssistantRoutes(StudioResource, BaseRoutes):
    def create(
        self,
        *,
        assistant_id: str,
        plan_id: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        examples: List[str],
        **kwargs,
    ) -> RouteResponse:
        body = self._create_body(
            plan_id=plan_id,
            name=name,
            description=description,
            examples=examples,
            **kwargs,
        )

        return self._post(path=f"/assistants/{assistant_id}/{self._module_name}", body=body, response_cls=RouteResponse)

    def list(
        self,
        *,
        assistant_id: str,
        name: str | NotGiven = NOT_GIVEN,
    ) -> ListRouteResponse:
        params = self._create_body(name=name)

        return self._get(
            path=f"/assistants/{assistant_id}/{self._module_name}", params=params, response_cls=ListRouteResponse
        )

    def retrieve(
        self,
        *,
        assistant_id: str,
        route_id: str,
    ) -> RouteResponse:
        return self._get(path=f"/assistants/{assistant_id}/{self._module_name}/{route_id}", response_cls=RouteResponse)

    def modify(
        self,
        *,
        assistant_id: str,
        route_id: str,
        description: str | NotGiven = NOT_GIVEN,
        examples: List[str] | NotGiven = NOT_GIVEN,
    ) -> RouteResponse:
        body = self._create_body(
            description=description,
            examples=examples,
        )

        return self._patch(
            path=f"/assistants/{assistant_id}/{self._module_name}/{route_id}", body=body, response_cls=RouteResponse
        )

    def delete(
        self,
        *,
        assistant_id: str,
        route_id: str,
    ):
        return self._delete(path=f"/assistants/{assistant_id}/{self._module_name}/{route_id}")


class AsyncAssistantRoutes(AsyncStudioResource, BaseRoutes):
    async def create(
        self,
        *,
        assistant_id: str,
        plan_id: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        examples: List[str],
        **kwargs,
    ) -> RouteResponse:
        body = self._create_body(
            plan_id=plan_id,
            name=name,
            description=description,
            examples=examples,
            **kwargs,
        )

        return await self._post(
            path=f"/assistants/{assistant_id}/{self._module_name}", body=body, response_cls=RouteResponse
        )

    async def list(
        self,
        *,
        assistant_id: str,
        name: str | NotGiven = NOT_GIVEN,
    ) -> ListRouteResponse:
        params = self._create_body(name=name)

        return await self._get(
            path=f"/assistants/{assistant_id}/{self._module_name}", params=params, response_cls=ListRouteResponse
        )

    async def retrieve(
        self,
        *,
        assistant_id: str,
        route_id: str,
    ) -> RouteResponse:
        return await self._get(
            path=f"/assistants/{assistant_id}/{self._module_name}/{route_id}", response_cls=RouteResponse
        )

    async def modify(
        self,
        *,
        assistant_id: str,
        route_id: str,
        description: str | NotGiven = NOT_GIVEN,
        examples: List[str] | NotGiven = NOT_GIVEN,
    ) -> RouteResponse:
        body = self._create_body(
            description=description,
            examples=examples,
        )

        return await self._patch(
            path=f"/assistants/{assistant_id}/{self._module_name}/{route_id}", body=body, response_cls=RouteResponse
        )

    async def delete(
        self,
        *,
        assistant_id: str,
        route_id: str,
    ):
        return await self._delete(path=f"/assistants/{assistant_id}/{self._module_name}/{route_id}")
