from abc import ABC, abstractmethod
from typing import Dict, Any

from ai21.resources.responses.gec_response import GECResponse


class GEC(ABC):
    _module_name = "gec"

    @abstractmethod
    def create(self, text: str, **kwargs) -> GECResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> GECResponse:
        return GECResponse.from_dict(json)

    def _create_body(self, text: str) -> Dict[str, Any]:
        return {"text": text}
