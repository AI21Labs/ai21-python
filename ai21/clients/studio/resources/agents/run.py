from __future__ import annotations

import asyncio
import time
from typing import List, Dict, Any

from ai21.clients.common.agents.run import BaseAgentRun
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models.agents import RunResponse
from ai21.types import NotGiven, NOT_GIVEN

DEFAULT_RUN_POLL_INTERVAL = 2.0
DEFAULT_RUN_POLL_TIMEOUT = 300.0
TERMINATED_RUN_STATUSES = {"completed", "failed", "cancelled", "expired"}


class AgentRun(StudioResource, BaseAgentRun):
    def create(
        self,
        agent_id: str,
        *,
        input: List[Dict[str, str]],
        verbose: bool = False,
        output_type: Dict[str, Any] | NotGiven = NOT_GIVEN,
        include: List[str] | NotGiven = NOT_GIVEN,
        structured_rag_enabled: bool = False,
        dynamic_planning_enabled: bool = False,
        response_language: str = "english",
        **kwargs,
    ) -> RunResponse:
        """Run an agent with the given input"""
        body = self._create_run_body(
            agent_id=agent_id,
            input=input,
            verbose=verbose,
            output_type=output_type,
            include=include,
            structured_rag_enabled=structured_rag_enabled,
            dynamic_planning_enabled=dynamic_planning_enabled,
            response_language=response_language,
            **kwargs,
        )

        # Use assistants API endpoint for running
        result = self._post(path=f"/{self._module_name}/{agent_id}/run", body=body, response_cls=RunResponse)
        assert result is not None  # response_cls is provided, so result should never be None
        return result

    def retrieve(self, run_id: str) -> RunResponse:
        """Retrieve a run by ID"""
        # Note: This would typically need a different endpoint structure
        # For now, assuming maestro-like endpoint
        result = self._get(path=f"/maestro/runs/{run_id}", response_cls=RunResponse)
        assert result is not None  # response_cls is provided, so result should never be None
        return result

    def poll_for_status(self, *, run_id: str, poll_interval_sec: float, poll_timeout_sec: float) -> RunResponse:
        """Poll for run completion"""
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
        agent_id: str,
        *,
        input: List[Dict[str, str]],
        verbose: bool = False,
        output_type: Dict[str, Any] | NotGiven = NOT_GIVEN,
        include: List[str] | NotGiven = NOT_GIVEN,
        structured_rag_enabled: bool = False,
        dynamic_planning_enabled: bool = False,
        response_language: str = "unset",
        poll_interval_sec: float = DEFAULT_RUN_POLL_INTERVAL,
        poll_timeout_sec: float = DEFAULT_RUN_POLL_TIMEOUT,
        **kwargs,
    ) -> RunResponse:
        """Create and poll an agent run until completion"""
        run = self.create(
            agent_id=agent_id,
            input=input,
            verbose=verbose,
            output_type=output_type,
            include=include,
            structured_rag_enabled=structured_rag_enabled,
            dynamic_planning_enabled=dynamic_planning_enabled,
            response_language=response_language,
            **kwargs,
        )

        return self.poll_for_status(
            run_id=str(run.id), poll_interval_sec=poll_interval_sec, poll_timeout_sec=poll_timeout_sec
        )


class AsyncAgentRun(AsyncStudioResource, BaseAgentRun):
    async def create(
        self,
        agent_id: str,
        *,
        input: List[Dict[str, str]],
        verbose: bool = False,
        output_type: Dict[str, Any] | NotGiven = NOT_GIVEN,
        include: List[str] | NotGiven = NOT_GIVEN,
        structured_rag_enabled: bool = False,
        dynamic_planning_enabled: bool = False,
        response_language: str = "unset",
        **kwargs,
    ) -> RunResponse:
        """Run an agent with the given input"""
        body = self._create_run_body(
            agent_id=agent_id,
            input=input,
            verbose=verbose,
            output_type=output_type,
            include=include,
            structured_rag_enabled=structured_rag_enabled,
            dynamic_planning_enabled=dynamic_planning_enabled,
            response_language=response_language,
            **kwargs,
        )

        result = await self._post(path=f"/{self._module_name}/{agent_id}/run", body=body, response_cls=RunResponse)
        assert result is not None  # response_cls is provided, so result should never be None
        return result

    async def retrieve(self, run_id: str) -> RunResponse:
        """Retrieve a run by ID"""
        result = await self._get(path=f"/maestro/runs/{run_id}", response_cls=RunResponse)
        assert result is not None  # response_cls is provided, so result should never be None
        return result

    async def poll_for_status(self, *, run_id: str, poll_interval_sec: float, poll_timeout_sec: float) -> RunResponse:
        """Poll for run completion"""
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
        agent_id: str,
        *,
        input: List[Dict[str, str]],
        verbose: bool = False,
        output_type: Dict[str, Any] | NotGiven = NOT_GIVEN,
        include: List[str] | NotGiven = NOT_GIVEN,
        structured_rag_enabled: bool = False,
        dynamic_planning_enabled: bool = False,
        response_language: str = "unset",
        poll_interval_sec: float = DEFAULT_RUN_POLL_INTERVAL,
        poll_timeout_sec: float = DEFAULT_RUN_POLL_TIMEOUT,
        **kwargs,
    ) -> RunResponse:
        """Create and poll an agent run until completion"""
        run = await self.create(
            agent_id=agent_id,
            input=input,
            verbose=verbose,
            output_type=output_type,
            include=include,
            structured_rag_enabled=structured_rag_enabled,
            dynamic_planning_enabled=dynamic_planning_enabled,
            response_language=response_language,
            **kwargs,
        )

        return await self.poll_for_status(
            run_id=str(run.id), poll_interval_sec=poll_interval_sec, poll_timeout_sec=poll_timeout_sec
        )
