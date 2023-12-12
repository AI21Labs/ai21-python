from abc import ABC, abstractmethod
from typing import List, Any, Dict, Optional

from ai21.resources.responses.embed_response import EmbedResponse


class Embed(ABC):
    _module_name = "embed"

    @abstractmethod
    def create(self, texts: List[str], *, type: Optional[str] = None, **kwargs) -> EmbedResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> EmbedResponse:
        return EmbedResponse.model_validate(json)
