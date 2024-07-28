from abc import ABC, abstractmethod
from typing import Dict, Any, cast

from ai21.models import GECResponse
from ai21.models._pydantic_compatibility import _from_dict


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
        return cast(_from_dict(obj=GECResponse, obj_dict=json), GECResponse)

    def _create_body(self, text: str, **kwargs) -> Dict[str, Any]:
        return {"text": text, **kwargs}
