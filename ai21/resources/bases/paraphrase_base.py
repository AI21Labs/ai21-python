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
        return ParaphraseResponse.from_dict(json)

    def _create_body(
        self,
        text: str,
        style: Optional[str],
        start_index: Optional[int],
        end_index: Optional[int],
    ) -> Dict[str, Any]:
        return {
            "text": text,
            "style": style,
            "startIndex": start_index,
            "endIndex": end_index,
        }
