from abc import ABC

from ai21.clients.common.maestro.run import BaseMaestroRun


class BaseMaestro(ABC):
    _module_name = "maestro"
    runs: BaseMaestroRun
