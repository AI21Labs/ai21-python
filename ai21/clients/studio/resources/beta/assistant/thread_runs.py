from __future__ import annotations

from typing import List

from ai21.clients.common.beta.assistant.runs import BaseRuns
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models.assistant.assistant import Optimization
from ai21.models.assistant.run import ToolOutput
from ai21.models.responses.run_response import RunResponse
from ai21.types import NotGiven, NOT_GIVEN


class ThreadRuns(StudioResource, BaseRuns):
    def create(
        self,
        *,
        thread_id: str,
        assistant_id: str,
        description: str | NotGiven = NOT_GIVEN,
        optimization: Optimization | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> RunResponse:
        body = self._create_body(
            thread_id=thread_id,
            assistant_id=assistant_id,
            description=description,
            optimization=optimization,
            **kwargs,
        )

        return self._post(path=f"/threads/{thread_id}/{self._module_name}", body=body, response_cls=RunResponse)

    def retrieve(
        self,
        *,
        thread_id: str,
        run_id: str,
    ) -> RunResponse:
        return self._get(path=f"/threads/{thread_id}/{self._module_name}/{run_id}", response_cls=RunResponse)

    def cancel(
        self,
        *,
        thread_id: str,
        run_id: str,
    ) -> RunResponse:
        return self._post(path=f"/threads/{thread_id}/{self._module_name}/{run_id}/cancel", response_cls=RunResponse)

    def submit_tool_outputs(self, *, thread_id: str, run_id: str, tool_outputs: List[ToolOutput]) -> RunResponse:
        body = dict(tool_outputs=tool_outputs)

        return self._post(
            path=f"/threads/{thread_id}/{self._module_name}/{run_id}/submit_tool_outputs",
            body=body,
            response_cls=RunResponse,
        )


class AsyncThreadRuns(AsyncStudioResource, BaseRuns):
    async def create(
        self,
        *,
        thread_id: str,
        assistant_id: str,
        description: str | NotGiven = NOT_GIVEN,
        optimization: Optimization | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> RunResponse:
        body = self._create_body(
            thread_id=thread_id,
            assistant_id=assistant_id,
            description=description,
            optimization=optimization,
            **kwargs,
        )

        return await self._post(path=f"/threads/{thread_id}/{self._module_name}", body=body, response_cls=RunResponse)

    async def retrieve(
        self,
        *,
        thread_id: str,
        run_id: str,
    ) -> RunResponse:
        return await self._get(path=f"/threads/{thread_id}/{self._module_name}/{run_id}", response_cls=RunResponse)

    async def cancel(
        self,
        *,
        thread_id: str,
        run_id: str,
    ) -> RunResponse:
        return await self._post(
            path=f"/threads/{thread_id}/{self._module_name}/{run_id}/cancel", response_cls=RunResponse
        )

    async def submit_tool_outputs(self, *, thread_id: str, run_id: str, tool_outputs: List[ToolOutput]) -> RunResponse:
        body = dict(tool_outputs=tool_outputs)

        return await self._post(
            path=f"/threads/{thread_id}/{self._module_name}/{run_id}/submit_tool_outputs",
            body=body,
            response_cls=RunResponse,
        )
