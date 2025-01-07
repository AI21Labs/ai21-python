from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List

from ai21.models.assistant.assistant import Optimization
from ai21.models.assistant.run import ToolOutput
from ai21.models.responses.run_response import RunResponse
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class BaseRuns(ABC):
    _module_name = "runs"

    @abstractmethod
    def create(
        self,
        *,
        thread_id: str,
        assistant_id: str,
        description: str | NotGiven = NOT_GIVEN,
        optimization: Optimization | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> RunResponse:
        pass

    def _create_body(
        self,
        *,
        thread_id: str,
        assistant_id: str,
        description: str | NotGiven,
        optimization: str | NotGiven,
        **kwargs,
    ) -> dict:
        return remove_not_given(
            {
                "thread_id": thread_id,
                "assistant_id": assistant_id,
                "description": description,
                "optimization": optimization,
                **kwargs,
            }
        )

    @abstractmethod
    def retrieve(
        self,
        *,
        thread_id: str,
        run_id: str,
    ) -> RunResponse:
        pass

    @abstractmethod
    def cancel(
        self,
        *,
        thread_id: str,
        run_id: str,
    ) -> RunResponse:
        pass

    @abstractmethod
    def submit_tool_outputs(self, *, thread_id: str, run_id: str, tool_outputs: List[ToolOutput]) -> RunResponse:
        pass

    @abstractmethod
    def _poll_for_status(
        self, *, thread_id: str, run_id: str, poll_interval: float, poll_timeout: float
    ) -> RunResponse:
        pass

    @abstractmethod
    def create_and_poll(
        self,
        *,
        thread_id: str,
        assistant_id: str,
        description: str | NotGiven,
        optimization: Optimization | NotGiven,
        poll_interval_sec: float,
        poll_timeout_sec: float,
        **kwargs,
    ) -> RunResponse:
        pass

    @abstractmethod
    def submit_input(self, *, thread_id: str, run_id: str, input: Any) -> RunResponse:
        pass

    @abstractmethod
    def submit_input_and_poll(
        self,
        *,
        thread_id: str,
        run_id: str,
        input: Any,
        poll_interval_sec: float,
        poll_timeout_sec: float,
    ) -> RunResponse:
        pass
