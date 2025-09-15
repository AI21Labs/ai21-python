from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Dict, Any

from ai21.models.agents.agent import RunResponse
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class BaseAgentRun(ABC):
    _module_name = "assistants"  # Uses assistants API underneath

    def _get_run_path(self, run_id: str) -> str:
        # Runs are handled by maestro system
        return f"/maestro/runs/{run_id}"

    def _create_run_body(
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
    ) -> dict:
        return remove_not_given(
            {
                "input": input,
                "verbose": verbose,
                "output_type": output_type,
                "include": include,
                "structured_rag_enabled": structured_rag_enabled,
                "dynamic_planning_enabled": dynamic_planning_enabled,
                "response_language": response_language,
                **kwargs,
            }
        )

    @abstractmethod
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
        agent_id: str,
        *,
        input: List[Dict[str, str]],
        verbose: bool = False,
        output_type: Dict[str, Any] | NotGiven = NOT_GIVEN,
        include: List[str] | NotGiven = NOT_GIVEN,
        structured_rag_enabled: bool = False,
        dynamic_planning_enabled: bool = False,
        response_language: str = "english",
        poll_interval_sec: float = 2.0,
        poll_timeout_sec: float = 300.0,
        **kwargs,
    ) -> RunResponse:
        pass