from __future__ import annotations

from typing import List, Any, Dict, Type

from pydantic import BaseModel

from ai21.clients.common.beta.assistant.plans import BasePlans
from ai21.clients.studio.resources.studio_resource import (
    AsyncStudioResource,
    StudioResource,
)
from ai21.models.responses.plan_response import PlanResponse, ListPlanResponse
from ai21.types import NotGiven, NOT_GIVEN


class AssistantPlans(StudioResource, BasePlans):
    def create(
        self,
        *,
        assistant_id: str,
        code: str,
        schemas: List[Dict[str, Any]] | List[Type[BaseModel]] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> PlanResponse:
        body = self._create_body(
            code=code,
            schemas=schemas,
            **kwargs,
        )

        return self._post(path=f"/assistants/{assistant_id}/{self._module_name}", body=body, response_cls=PlanResponse)

    def list(
        self,
        *,
        assistant_id: str,
    ) -> ListPlanResponse:
        return self._get(path=f"/assistants/{assistant_id}/{self._module_name}", response_cls=ListPlanResponse)

    def retrieve(
        self,
        *,
        assistant_id: str,
        plan_id: str,
    ) -> PlanResponse:
        return self._get(path=f"/assistants/{assistant_id}/{self._module_name}/{plan_id}", response_cls=PlanResponse)

    def modify(
        self,
        *,
        assistant_id: str,
        plan_id: str,
        code: str,
        schemas: List[Dict[str, Any]] | List[Type[BaseModel]] | NotGiven = NOT_GIVEN,
    ) -> PlanResponse:
        body = self._create_body(
            code=code,
            schemas=schemas,
        )

        return self._patch(
            path=f"/assistants/{assistant_id}/{self._module_name}/{plan_id}", body=body, response_cls=PlanResponse
        )


class AsyncAssistantPlans(AsyncStudioResource, BasePlans):
    async def create(
        self,
        *,
        assistant_id: str,
        code: str,
        schemas: List[Dict[str, Any]] | List[Type[BaseModel]] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> PlanResponse:
        body = self._create_body(
            code=code,
            schemas=schemas,
            **kwargs,
        )

        return await self._post(
            path=f"/assistants/{assistant_id}/{self._module_name}", body=body, response_cls=PlanResponse
        )

    async def list(
        self,
        *,
        assistant_id: str,
    ) -> ListPlanResponse:
        return await self._get(path=f"/assistants/{assistant_id}/{self._module_name}", response_cls=ListPlanResponse)

    async def retrieve(
        self,
        *,
        assistant_id: str,
        plan_id: str,
    ) -> PlanResponse:
        return await self._get(
            path=f"/assistants/{assistant_id}/{self._module_name}/{plan_id}", response_cls=PlanResponse
        )

    async def modify(
        self,
        *,
        assistant_id: str,
        plan_id: str,
        code: str,
        schemas: List[Dict[str, Any]] | List[Type[BaseModel]] | NotGiven = NOT_GIVEN,
    ) -> PlanResponse:
        body = self._create_body(
            code=code,
            schemas=schemas,
        )

        return await self._patch(
            path=f"/assistants/{assistant_id}/{self._module_name}/{plan_id}", body=body, response_cls=PlanResponse
        )
