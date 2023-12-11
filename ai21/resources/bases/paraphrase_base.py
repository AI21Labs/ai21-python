from abc import ABC, abstractmethod
from typing import Optional, Any, Dict

from ai21.resources.responses.paraphrase_response import ParaphraseResponse


class Paraphrase(ABC):
    _module_name = "paraphrase"

    @abstractmethod
    def create(
        self,
        text: str,
        *,
        style: Optional[str] = None,
        start_index: Optional[int] = 0,
        end_index: Optional[int] = None,
        **kwargs,
    ) -> ParaphraseResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> ParaphraseResponse:
        return ParaphraseResponse.model_validate(json)
