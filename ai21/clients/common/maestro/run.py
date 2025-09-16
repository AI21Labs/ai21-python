from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Union

from ai21.models.maestro.run import (
    Budget,
    DEFAULT_RUN_POLL_INTERVAL,
    DEFAULT_RUN_POLL_TIMEOUT,
    MaestroMessage,
    OutputOptions,
    Requirement,
    RunResponse,
    ToolResources,
    ToolDefinition,
)
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class BaseMaestroRun(ABC):
    _module_name = "maestro/runs"

    def _create_body(
        self,
        *,
        input: Union[str, List[MaestroMessage]],
        models: Union[List[str], NotGiven],
        tools: Union[List[ToolDefinition], NotGiven],
        tool_resources: Union[ToolResources, NotGiven],
        requirements: Union[List[Requirement], NotGiven],
        budget: Union[Budget, NotGiven],
        include: Union[List[OutputOptions], NotGiven],
        response_language: Union[str, NotGiven],
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
                "response_language": response_language,
                **kwargs,
            }
        )

    @abstractmethod
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
        pass
