from abc import ABC, abstractmethod
from typing import List, Dict, Any

from ai21.models.maestro.run import RunResponse
from ai21.types import NOT_GIVEN, NotGiven


class BaseAgentRun(ABC):
    """Base class for agent run operations"""

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
        """Create an agent run"""
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
        """Create and poll an agent run"""
        pass
