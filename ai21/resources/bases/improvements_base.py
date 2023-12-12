from abc import ABC, abstractmethod
from typing import Any, Dict, List

from ai21.resources.responses.improvement_response import ImprovementsResponse


class Improvements(ABC):
    _module_name = "improvements"

    @abstractmethod
    def create(self, text: str, types: List[str], **kwargs) -> ImprovementsResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> ImprovementsResponse:
        return ImprovementsResponse.model_validate(json)
