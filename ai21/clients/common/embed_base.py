from abc import ABC, abstractmethod
from typing import List, Any, Dict, Optional

from ai21.models.embed_type import EmbedType
from ai21.models.responses.embed_response import EmbedResponse


class Embed(ABC):
    _module_name = "embed"

    @abstractmethod
    def create(self, texts: List[str], *, type: Optional[EmbedType] = None, **kwargs) -> EmbedResponse:
        """

        :param texts: A list of strings, each representing a document or segment of text to be embedded.
        :param type: For retrieval/search use cases, indicates whether the texts that were
         sent are segments or the query.
        :param kwargs:
        :return:
        """
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> EmbedResponse:
        return EmbedResponse.from_dict(json)

    def _create_body(self, texts: List[str], type: Optional[str]) -> Dict[str, Any]:
        return {"texts": texts, "type": type}
