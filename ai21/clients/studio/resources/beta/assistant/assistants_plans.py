from __future__ import annotations

from ai21.clients.common.beta.assistant.plans import BasePlans
from ai21.clients.studio.resources.studio_resource import (
    AsyncStudioResource,
    StudioResource,
)
from ai21.models.responses.plan_response import PlanResponse, ListPlanResponse


class AssistantPlans(StudioResource, BasePlans):
    def create(
        self,
        *,
        assistant_id: str,
        code: str,
        **kwargs,
    ) -> PlanResponse:
        body = self._create_body(
            code=code,
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
    ) -> PlanResponse:
        body = dict(code=code)

        return self._patch(
            path=f"/assistants/{assistant_id}/{self._module_name}/{plan_id}", body=body, response_cls=PlanResponse
        )


class AsyncAssistantPlans(AsyncStudioResource, BasePlans):
    async def create(
        self,
        *,
        assistant_id: str,
        code: str,
        **kwargs,
    ) -> PlanResponse:
        body = self._create_body(
            code=code,
            **kwargs,
        )

        return self._post(path=f"/assistants/{assistant_id}/{self._module_name}", body=body, response_cls=PlanResponse)

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
    ) -> PlanResponse:
        body = dict(code=code)

        return await self._patch(
            path=f"/assistants/{assistant_id}/{self._module_name}/{plan_id}", body=body, response_cls=PlanResponse
        )
