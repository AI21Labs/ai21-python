from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Dict, Any

from ai21.models._pydantic_compatibility import _to_dict
from ai21.models.chat import ChatMessage
from ai21.models.maestro.runs import (
    Tool,
    ToolResources,
    Budget,
    RunResponse,
    DEFAULT_RUN_POLL_INTERVAL,
    DEFAULT_RUN_POLL_TIMEOUT,
)
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class BaseMaestroRun(ABC):
    _module_name = "maestro/runs"

    def _create_body(
        self,
        *,
        instruction: str | NotGiven,
        messages: List[ChatMessage] | NotGiven,
        output_type: Dict[str, Any] | NotGiven,
        models: List[str] | NotGiven,
        tools: List[Tool] | NotGiven,
        tool_resources: ToolResources | NotGiven,
        context: Dict[str, Any] | NotGiven,
        requirements: List[str] | NotGiven,
        budget: Budget | NotGiven,
        **kwargs,
    ) -> dict:
        messages_payload = remove_not_given({"messages": messages, "instruction": instruction})
        if not messages_payload:
            # not messages nor instruction were given
            raise ValueError("Must provide either `messages` or `instruction`")
        elif len(messages_payload.keys()) > 1:
            # both messages and instruction were given
            raise ValueError("Must provide only one of `messages` or `instruction`")
        elif "instruction" in messages_payload:
            # instruction was given and should be modified accordingly
            messages = [ChatMessage(role="user", content=instruction)]

        return remove_not_given(
            {
                "messages": [_to_dict(message) for message in messages],
                "output_type": output_type,
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
        instruction: str | NotGiven = NOT_GIVEN,
        messages: List[ChatMessage] | NotGiven = NOT_GIVEN,
        output_type: Dict[str, Any] | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
        context: Dict[str, Any] | NotGiven = NOT_GIVEN,
        requirements: List[str] | NotGiven = NOT_GIVEN,
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
        instruction: str | NotGiven = NOT_GIVEN,
        messages: List[ChatMessage] | NotGiven = NOT_GIVEN,
        output_type: Dict[str, Any] | NotGiven = NOT_GIVEN,
        models: List[str] | NotGiven = NOT_GIVEN,
        tools: List[Tool] | NotGiven = NOT_GIVEN,
        tool_resources: ToolResources | NotGiven = NOT_GIVEN,
        context: Dict[str, Any] | NotGiven = NOT_GIVEN,
        requirements: List[str] | NotGiven = NOT_GIVEN,
        budget: Budget | NotGiven = NOT_GIVEN,
        poll_interval_sec: float = DEFAULT_RUN_POLL_INTERVAL,
        poll_timeout_sec: float = DEFAULT_RUN_POLL_TIMEOUT,
        **kwargs,
    ) -> RunResponse:
        pass
