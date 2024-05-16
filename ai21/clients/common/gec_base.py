from abc import ABC, abstractmethod
from typing import Dict, Any

from ai21.models import GECResponse


class GEC(ABC):
    _module_name = "gec"

    @abstractmethod
    def create(self, text: str, **kwargs) -> GECResponse:
        """

        :param text: The input text to be corrected.
        :param kwargs:
        :return:
        """
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> GECResponse:
        return GECResponse.from_dict(json)

    def _create_body(self, text: str, **kwargs) -> Dict[str, Any]:
        return {"text": text, **kwargs}
