from typing import List, Dict, Any

from pydantic import Field

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.agents import Agent
from ai21.models.maestro.run import MaestroMessage
from typing import Optional


class AgentToMaestroRunConverter(AI21BaseModel):
    """Pydantic model that converts agent run parameters to maestro run parameters"""

    # Agent inputs
    agent_id: str
    input: List[Dict[str, str]]
    verbose: bool = False
    output_type: Optional[Dict[str, Any]] = None
    include: Optional[List[str]] = None
    structured_rag_enabled: bool = False
    dynamic_planning_enabled: bool = False
    response_language: str = "english"

    # Agent configuration (will be populated from agent fetch)
    agent_models: Optional[List[str]] = None
    agent_tools: Optional[List[Dict[str, Any]]] = None
    agent_tool_resources: Optional[Dict[str, Any]] = None
    agent_requirements: Optional[List[Dict[str, Any]]] = None
    agent_budget: Optional[str] = None

    # Computed maestro parameters
    maestro_input: List[MaestroMessage] = Field(default_factory=list)
    maestro_models: Optional[List[str]] = None
    maestro_tools: Optional[List[Dict[str, Any]]] = None
    maestro_tool_resources: Optional[Dict[str, Any]] = None
    maestro_requirements: Optional[List[Dict[str, Any]]] = None
    maestro_budget: Optional[str] = None
    maestro_include: Optional[List[str]] = None

    def model_post_init(self, __context) -> None:
        """Convert agent parameters to maestro parameters after initialization"""
        # Convert input messages
        self.maestro_input = [MaestroMessage(role=msg["role"], content=msg["content"]) for msg in self.input]

        # Map agent configuration to maestro parameters
        self.maestro_models = self.agent_models
        self.maestro_tools = self.agent_tools
        self.maestro_tool_resources = self.agent_tool_resources
        self.maestro_requirements = self.agent_requirements
        self.maestro_budget = self.agent_budget
        self.maestro_include = self.include

    @classmethod
    def from_agent_and_params(
        cls,
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
    ) -> "AgentToMaestroRunConverter":
        """Create converter from agent configuration and run parameters"""
        agent_requirements = None
        if agent.requirements:
            agent_requirements = [req.model_dump() for req in agent.requirements]

        return cls(
            agent_id=agent_id,
            input=input,
            verbose=verbose,
            output_type=output_type,
            include=include,
            structured_rag_enabled=structured_rag_enabled,
            dynamic_planning_enabled=dynamic_planning_enabled,
            response_language=response_language,
            agent_models=agent.models,
            agent_tools=agent.tools,
            agent_tool_resources=agent.tool_resources,
            agent_requirements=agent_requirements,
            agent_budget=agent.budget.value if agent.budget else None,
            **kwargs,
        )

    def to_maestro_create_params(self) -> dict:
        """Convert to parameters for maestro.runs.create()"""
        params = {
            "input": self.maestro_input,
            "models": self.maestro_models,
            "tools": self.maestro_tools,
            "tool_resources": self.maestro_tool_resources,
            "requirements": self.maestro_requirements,
            "budget": self.maestro_budget,
            "include": self.maestro_include,
            "response_language": self.response_language,
        }
        # Remove None values
        return {k: v for k, v in params.items() if v is not None}
