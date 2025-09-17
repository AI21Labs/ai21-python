from abc import ABC, abstractmethod
from typing import List, Dict, Any, Union, Optional

from ai21.models.agents import Agent
from ai21.models.maestro.run import RunResponse
from ai21.types import NOT_GIVEN, NotGiven


class BaseAgentRun(ABC):
    def _create_agent_to_maestro_converter(
        self,
        agent: Agent,
        agent_id: str,
        input: List[Dict[str, str]],
        verbose: bool = False,
        output_type: Optional[Dict[str, Any]] = None,
        include: Optional[List[str]] = None,
        structured_rag_enabled: bool = False,
        dynamic_planning_enabled: bool = False,
        response_language: str = "english",
        **kwargs,
    ):
        """Create converter from agent configuration and run parameters

        This method needs to be imported and used by subclasses since AgentToMaestroRunConverter
        is defined in the studio-specific utils module.
        """
        # Import here to avoid circular dependencies
        from ai21.clients.studio.resources.agents.utils import AgentToMaestroRunConverter

        return AgentToMaestroRunConverter.from_agent_and_params(
            agent=agent,
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
