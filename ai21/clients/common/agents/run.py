from abc import ABC
from typing import List

from ai21.models.agents import Agent
from ai21.models.agents.agent import AgentRequirement
from ai21.models.maestro.run import Requirement
from ai21.utils.typing import remove_not_given


class BaseAgentRun(ABC):
    def _convert_requirements(self, requirements: List[AgentRequirement]):
        """Convert agent requirements to maestro requirements, filtering out invalid ones."""
        if not requirements:
            return None

        converted_requirements = []
        for req in requirements:
            if req.title and req.description and req.type:
                converted_requirements.append(
                    Requirement(
                        name=req.title,
                        description=req.description,
                        is_mandatory=req.type == "mandatory",
                    )
                )

        return converted_requirements or None

    def convert_agent_to_maestro_run_payload(
        self,
        agent: Agent,
        **kwargs,
    ):
        return remove_not_given(
            {
                "models": agent.models,
                "tools": agent.tools,
                "tool_resources": agent.tool_resources,
                "requirements": self._convert_requirements(agent.requirements),
                "budget": agent.budget,
                "response_language": agent.response_language,
                **kwargs,
            }
        )
