from abc import ABC, abstractmethod
from typing import Any, Dict

from ai21.models import DocumentType, SegmentationResponse


class Segmentation(ABC):
    _module_name = "segmentation"

    @abstractmethod
    def create(self, source: str, source_type: DocumentType, **kwargs) -> SegmentationResponse:
        """

        :param source: Raw input text, or URL of a web page.
        :param source_type: The type of the source - either TEXT or URL.
        :param kwargs:
        :return:
        """
        pass

    def _create_body(self, source: str, source_type: str, **kwargs) -> Dict[str, Any]:
        return {"source": source, "sourceType": source_type, **kwargs}
