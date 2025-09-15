from abc import ABC

from ai21.clients.common.agents.run import BaseAgentRun


class BaseAgents(ABC):
    _module_name = "assistants"
    runs: BaseAgentRun
