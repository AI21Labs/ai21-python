from abc import ABC, abstractmethod
from typing import Any, Dict

from ai21.resources.responses.segmentation_response import SegmentationResponse


class Segmentation(ABC):
    _module_name = "segmentation"

    @abstractmethod
    def create(self, source: str, source_type: str):
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> SegmentationResponse:
        return SegmentationResponse.model_validate(json)

    def _create_body(self, source: str, source_type: str, **kwargs) -> Dict[str, Any]:
        return {"source": source, "sourceType": source_type, **kwargs}
