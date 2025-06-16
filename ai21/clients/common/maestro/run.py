from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from ai21.models.maestro.run import (
    Budget,
    DEFAULT_RUN_POLL_INTERVAL,
    DEFAULT_RUN_POLL_TIMEOUT,
    MaestroMessage,
    OutputOptions,
    Requirement,
    RunResponse,
    Tool,
    ToolResources,
)
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class BaseMaestroRun(ABC):
    _module_name = "maestro/runs"

    def _create_body(
        self,
        *,
        input: str | List[MaestroMessage],
        models: List[str] | NotGiven,
        tools: List[Tool] | NotGiven,
        tool_resources: ToolResources | NotGiven,
        requirements: List[Requirement] | NotGiven,
        budget: Budget | NotGiven,
        include: List[OutputOptions] | NotGiven,
        **kwargs,
    ) -> dict:
        return remove_not_given(
            {
                "input": input,
                "models": models,
                "tools": tools,
                "tool_resources": tool_resources,
                "requirements": requirements,
                "budget": budget,
                "include": include,
                **kwargs,
            }
        )

    @abstractmethod
    def create(
        self,
        *,
        input: str | List[MaestroMessage],
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
        requirements: List[Requirement] | NotGiven = NOT_GIVEN,
        budget: Budget | NotGiven = NOT_GIVEN,
        include: List[OutputOptions] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> RunResponse:
        pass

    @abstractmethod
    def retrieve(self, run_id: str) -> RunResponse:
        pass

    @abstractmethod
    def poll_for_status(self, *, run_id: str, poll_interval_sec: float, poll_timeout_sec: float) -> RunResponse:
        pass

    @abstractmethod
    def create_and_poll(
        self,
        *,
        input: str | List[MaestroMessage],
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
        requirements: List[Requirement] | NotGiven = NOT_GIVEN,
        budget: Budget | NotGiven = NOT_GIVEN,
        include: List[OutputOptions] | NotGiven = NOT_GIVEN,
        poll_interval_sec: float = DEFAULT_RUN_POLL_INTERVAL,
        poll_timeout_sec: float = DEFAULT_RUN_POLL_TIMEOUT,
        **kwargs,
    ) -> RunResponse:
        pass
