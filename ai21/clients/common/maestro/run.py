from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Dict, Any

from ai21.models.chat import ChatMessage
from ai21.models.maestro.run import (
    Tool,
    ToolResources,
    RunResponse,
    DEFAULT_RUN_POLL_INTERVAL,
    DEFAULT_RUN_POLL_TIMEOUT,
    Requirement,
    Budget,
)
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class BaseMaestroRun(ABC):
    _module_name = "maestro/runs"

    def _create_body(
        self,
        *,
        input: str | List[ChatMessage],
        models: List[str] | NotGiven,
        tools: List[Tool] | NotGiven,
        tool_resources: ToolResources | NotGiven,
        context: Dict[str, Any] | NotGiven,
        requirements: List[Requirement] | NotGiven,
        budget: Budget | NotGiven,
        **kwargs,
    ) -> dict:
        return remove_not_given(
            {
                "input": input,
                "models": models,
                "tools": tools,
                "tool_resources": tool_resources,
                "context": context,
                "requirements": requirements,
                "budget": budget,
                **kwargs,
            }
        )

    @abstractmethod
    def create(
        self,
        *,
        input: str | List[ChatMessage],
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
        context: Dict[str, Any] | NotGiven = NOT_GIVEN,
        requirements: List[Requirement] | NotGiven = NOT_GIVEN,
        budget: Budget | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> RunResponse:
        pass

    @abstractmethod
    def retrieve(self, run_id: str) -> RunResponse:
        pass

    @abstractmethod
    def _poll_for_status(self, *, run_id: str, poll_interval: float, poll_timeout: float) -> RunResponse:
        pass

    @abstractmethod
    def create_and_poll(
        self,
        *,
        input: str | List[ChatMessage],
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
        context: Dict[str, Any] | NotGiven = NOT_GIVEN,
        requirements: List[Requirement] | NotGiven = NOT_GIVEN,
        budget: Budget | NotGiven = NOT_GIVEN,
        poll_interval_sec: float = DEFAULT_RUN_POLL_INTERVAL,
        poll_timeout_sec: float = DEFAULT_RUN_POLL_TIMEOUT,
        **kwargs,
    ) -> RunResponse:
        pass
