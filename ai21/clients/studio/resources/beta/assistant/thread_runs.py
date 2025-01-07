from __future__ import annotations

import asyncio
import time
from typing import List

from ai21.clients.common.beta.assistant.runs import BaseRuns
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models.assistant.assistant import Optimization
from ai21.models.assistant.run import (
    ToolOutput,
    TERMINATED_RUN_STATUSES,
    DEFAULT_RUN_POLL_INTERVAL,
    DEFAULT_RUN_POLL_TIMEOUT,
)
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

    def _poll_for_status(
        self, *, thread_id: str, run_id: str, poll_interval: float, poll_timeout: float
    ) -> RunResponse:
        start_time = time.time()

        while True:
            run = self.retrieve(thread_id=thread_id, run_id=run_id)

            if run.status in TERMINATED_RUN_STATUSES:
                return run

            if (time.time() - start_time) > poll_timeout:
                return run

            time.sleep(poll_interval)

    def create_and_poll(
        self,
        *,
        thread_id: str,
        assistant_id: str,
        description: str | NotGiven = NOT_GIVEN,
        optimization: Optimization | NotGiven = NOT_GIVEN,
        poll_interval: float = DEFAULT_RUN_POLL_INTERVAL,
        poll_timeout: float = DEFAULT_RUN_POLL_TIMEOUT,
        **kwargs,
    ) -> RunResponse:
        """
        Create a run and poll for its status until it is no longer in progress or the timeout is reached.

        Args:
            thread_id: The ID of the thread.
            assistant_id: The ID of the assistant.
            description: The description of the run.
            optimization: The optimization level to use.
            poll_interval: The interval in seconds to poll for the run status.
            poll_timeout: The timeout in seconds to wait for the run to complete.

        Returns:
            The run response.
        """
        run = self.create(
            thread_id=thread_id, assistant_id=assistant_id, description=description, optimization=optimization, **kwargs
        )

        return self._poll_for_status(
            thread_id=thread_id, run_id=run.id, poll_interval=poll_interval, poll_timeout=poll_timeout
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

    async def _poll_for_status(
        self, *, thread_id: str, run_id: str, poll_interval: float, poll_timeout: float
    ) -> RunResponse:
        start_time = time.time()

        while True:
            run = await self.retrieve(thread_id=thread_id, run_id=run_id)

            if run.status in TERMINATED_RUN_STATUSES:
                return run

            if (time.time() - start_time) > poll_timeout:
                return run

            await asyncio.sleep(poll_interval)

    async def create_and_poll(
        self,
        *,
        thread_id: str,
        assistant_id: str,
        description: str | NotGiven = NOT_GIVEN,
        optimization: Optimization | NotGiven = NOT_GIVEN,
        poll_interval: float = DEFAULT_RUN_POLL_INTERVAL,
        poll_timeout: float = DEFAULT_RUN_POLL_TIMEOUT,
        **kwargs,
    ) -> RunResponse:
        """
        Create a run and poll for its status until it is no longer in progress or the timeout is reached.

        Args:
            thread_id: The ID of the thread.
            assistant_id: The ID of the assistant.
            description: The description of the run.
            optimization: The optimization level to use.
            poll_interval: The interval in seconds to poll for the run status.
            poll_timeout: The timeout in seconds to wait for the run to complete.

        Returns:
            The run response.
        """
        run = await self.create(
            thread_id=thread_id, assistant_id=assistant_id, description=description, optimization=optimization, **kwargs
        )

        return await self._poll_for_status(
            thread_id=thread_id, run_id=run.id, poll_interval=poll_interval, poll_timeout=poll_timeout
        )
