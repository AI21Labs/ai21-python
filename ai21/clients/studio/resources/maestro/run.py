from __future__ import annotations

import asyncio
import time
from typing import List, Union

from ai21.clients.common.maestro.run import BaseMaestroRun
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models.maestro.run import (
    Budget,
    DEFAULT_RUN_POLL_INTERVAL,
    DEFAULT_RUN_POLL_TIMEOUT,
    MaestroMessage,
    OutputOptions,
    Requirement,
    RunResponse,
    TERMINATED_RUN_STATUSES,
    ToolResources,
    ToolDefinition,
)
from ai21.types import NotGiven, NOT_GIVEN


class MaestroRun(StudioResource, BaseMaestroRun):
    def create(
        self,
        *,
        input: Union[str, List[MaestroMessage]],
        models: Union[List[str], NotGiven] = NOT_GIVEN,
        tools: Union[List[ToolDefinition], NotGiven] = NOT_GIVEN,
        tool_resources: Union[ToolResources, NotGiven] = NOT_GIVEN,
        requirements: Union[List[Requirement], NotGiven] = NOT_GIVEN,
        budget: Union[Budget, NotGiven] = NOT_GIVEN,
        include: Union[List[OutputOptions], NotGiven] = NOT_GIVEN,
        response_language: Union[str, NotGiven] = NOT_GIVEN,
        **kwargs,
    ) -> RunResponse:
        body = self._create_body(
            input=input,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            requirements=requirements,
            budget=budget,
            include=include,
            response_language=response_language,
            **kwargs,
        )

        return self._post(path=f"/{self._module_name}", body=body, response_cls=RunResponse)

    def retrieve(
        self,
        run_id: str,
    ) -> RunResponse:
        return self._get(path=f"/{self._module_name}/{run_id}", response_cls=RunResponse)

    def poll_for_status(self, *, run_id: str, poll_interval_sec: float, poll_timeout_sec: float) -> RunResponse:
        start_time = time.time()

        while True:
            run = self.retrieve(run_id)

            if run.status in TERMINATED_RUN_STATUSES:
                return run

            if (time.time() - start_time) >= poll_timeout_sec:
                raise TimeoutError(f"Timeout of {poll_timeout_sec} while polling for status of run with id {run_id}")

            time.sleep(poll_interval_sec)

    def create_and_poll(
        self,
        *,
        input: Union[str, List[MaestroMessage]],
        models: Union[List[str], NotGiven] = NOT_GIVEN,
        tools: Union[List[ToolDefinition], NotGiven] = NOT_GIVEN,
        tool_resources: Union[ToolResources, NotGiven] = NOT_GIVEN,
        requirements: Union[List[Requirement], NotGiven] = NOT_GIVEN,
        budget: Union[Budget, NotGiven] = NOT_GIVEN,
        include: Union[List[OutputOptions], NotGiven] = NOT_GIVEN,
        response_language: Union[str, NotGiven] = NOT_GIVEN,
        poll_interval_sec: float = DEFAULT_RUN_POLL_INTERVAL,
        poll_timeout_sec: float = DEFAULT_RUN_POLL_TIMEOUT,
        **kwargs,
    ) -> RunResponse:
        run = self.create(
            input=input,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            requirements=requirements,
            budget=budget,
            include=include,
            response_language=response_language,
            **kwargs,
        )

        return self.poll_for_status(
            run_id=run.id, poll_interval_sec=poll_interval_sec, poll_timeout_sec=poll_timeout_sec
        )


class AsyncMaestroRun(AsyncStudioResource, BaseMaestroRun):
    async def create(
        self,
        *,
        input: Union[str, List[MaestroMessage]],
        models: Union[List[str], NotGiven] = NOT_GIVEN,
        tools: Union[List[ToolDefinition], NotGiven] = NOT_GIVEN,
        tool_resources: Union[ToolResources, NotGiven] = NOT_GIVEN,
        requirements: Union[List[Requirement], NotGiven] = NOT_GIVEN,
        budget: Union[Budget, NotGiven] = NOT_GIVEN,
        include: Union[List[OutputOptions], NotGiven] = NOT_GIVEN,
        response_language: Union[str, NotGiven] = NOT_GIVEN,
        **kwargs,
    ) -> RunResponse:
        body = self._create_body(
            input=input,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            requirements=requirements,
            budget=budget,
            include=include,
            response_language=response_language,
            **kwargs,
        )

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=RunResponse)

    async def retrieve(
        self,
        run_id: str,
    ) -> RunResponse:
        return await self._get(path=f"/{self._module_name}/{run_id}", response_cls=RunResponse)

    async def poll_for_status(self, *, run_id: str, poll_interval_sec: float, poll_timeout_sec: float) -> RunResponse:
        start_time = time.time()

        while True:
            run = await self.retrieve(run_id)

            if run.status in TERMINATED_RUN_STATUSES:
                return run

            if (time.time() - start_time) >= poll_timeout_sec:
                raise TimeoutError(f"Timeout of {poll_timeout_sec} while polling for status of run with id {run_id}")

            await asyncio.sleep(poll_interval_sec)

    async def create_and_poll(
        self,
        *,
        input: Union[str, List[MaestroMessage]],
        models: Union[List[str], NotGiven] = NOT_GIVEN,
        tools: Union[List[ToolDefinition], NotGiven] = NOT_GIVEN,
        tool_resources: Union[ToolResources, NotGiven] = NOT_GIVEN,
        requirements: Union[List[Requirement], NotGiven] = NOT_GIVEN,
        budget: Union[Budget, NotGiven] = NOT_GIVEN,
        include: Union[List[OutputOptions], NotGiven] = NOT_GIVEN,
        poll_interval_sec: float = DEFAULT_RUN_POLL_INTERVAL,
        poll_timeout_sec: float = DEFAULT_RUN_POLL_TIMEOUT,
        response_language: Union[str, NotGiven] = NOT_GIVEN,
        **kwargs,
    ) -> RunResponse:
        run = await self.create(
            input=input,
            models=models,
            tools=tools,
            tool_resources=tool_resources,
            requirements=requirements,
            budget=budget,
            include=include,
            response_language=response_language,
            **kwargs,
        )

        return await self.poll_for_status(
            run_id=run.id, poll_interval_sec=poll_interval_sec, poll_timeout_sec=poll_timeout_sec
        )
