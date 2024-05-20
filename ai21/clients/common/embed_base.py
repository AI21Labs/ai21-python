from abc import ABC, abstractmethod
from typing import List, Any, Dict, Optional

from ai21.models import EmbedType, EmbedResponse


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

    def _create_body(self, texts: List[str], type: Optional[str], **kwargs) -> Dict[str, Any]:
        return {"texts": texts, "type": type, **kwargs}
