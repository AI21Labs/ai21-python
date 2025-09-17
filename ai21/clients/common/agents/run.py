from abc import ABC, abstractmethod
from typing import List, Dict, Any, Union, Optional

from ai21.models.agents import Agent
from ai21.models.maestro.run import Requirement, RunResponse
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class BaseAgentRun(ABC):
    def convert_agent_to_maestro_run_payload(
        self,
        agent: Agent,
        **kwargs,
    ):
        return remove_not_given(
            dict(
                models=agent.models,
                tools=agent.tools,
                tool_resources=agent.tool_resources,
                requirements=agent.requirements,
                budget=agent.budget,
                response_language=agent.response_language,
                **kwargs,
            )
        )
