from __future__ import annotations

import inspect
from abc import ABC, abstractmethod
from typing import List, Dict, Any, get_origin, get_args, Optional

from pydantic import BaseModel

from ai21.models._pydantic_compatibility import _to_dict, _to_schema
from ai21.models.chat import ChatMessage
from ai21.models.maestro.run import (
    Tool,
    ToolResources,
    Budget,
    RunResponse,
    DEFAULT_RUN_POLL_INTERVAL,
    DEFAULT_RUN_POLL_TIMEOUT,
    OutputType,
)
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


def _primitive_to_schema(output_type):
    type_mapping = {
        int: "integer",
        float: "number",
        str: "string",
        bool: "boolean",
    }

    if output_type in type_mapping:
        return {"type": type_mapping[output_type]}

    origin = get_origin(output_type)
    args = get_args(output_type)

    if origin is list and len(args) == 1 and args[0] in type_mapping:
        return {"type": "array", "items": {"type": type_mapping[args[0]]}}


class BaseMaestroRun(ABC):
    _module_name = "maestro/runs"

    def _output_type_to_json_schema(self, output_type: OutputType | NotGiven) -> Optional[Dict[str, Any]]:
        if not output_type or isinstance(output_type, NotGiven):
            return NOT_GIVEN

        if inspect.isclass(output_type) and issubclass(output_type, BaseModel):
            result = _to_schema(output_type)
        else:
            result = _primitive_to_schema(output_type)

        if not result:
            raise ValueError(
                "Unsupported type. Supported types are: primitives types, List of primitive types, json schema dict, "
                "and pydantic models."
            )

        return result

    def _create_body(
        self,
        *,
        messages: List[ChatMessage],
        output_type: OutputType | NotGiven,
        models: List[str] | NotGiven,
        tools: List[Tool] | NotGiven,
        tool_resources: ToolResources | NotGiven,
        context: Dict[str, Any] | NotGiven,
        requirements: List[str] | NotGiven,
        budget: Budget | NotGiven,
        **kwargs,
    ) -> dict:
        return remove_not_given(
            {
                "messages": [_to_dict(message) for message in messages],
                "output_type": self._output_type_to_json_schema(output_type),
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
        messages: List[ChatMessage],
        output_type: OutputType | NotGiven = NOT_GIVEN,
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
        messages: List[ChatMessage],
        output_type: OutputType | NotGiven = NOT_GIVEN,
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
