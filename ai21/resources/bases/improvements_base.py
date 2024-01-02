from abc import ABC, abstractmethod
from typing import Any, Dict, List

from ai21.models import ImprovementType
from ai21.models.responses.improvement_response import ImprovementsResponse


class Improvements(ABC):
    _module_name = "improvements"

    @abstractmethod
    def create(self, text: str, types: List[ImprovementType], **kwargs) -> ImprovementsResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> ImprovementsResponse:
        return ImprovementsResponse.from_dict(json)

    def _create_body(self, text: str, types: List[str]) -> Dict[str, Any]:
        return {"text": text, "types": types}
