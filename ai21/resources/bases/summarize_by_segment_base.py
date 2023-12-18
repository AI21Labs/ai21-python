from abc import ABC, abstractmethod
from typing import Optional, Any, Dict

from ai21.resources.responses.summarize_by_segment_response import (
    SummarizeBySegmentResponse,
)


class SummarizeBySegment(ABC):
    _module_name = "summarize-by-segment"

    @abstractmethod
    def create(
        self,
        source: str,
        source_type: str,
        *,
        focus: Optional[str] = None,
        **kwargs,
    ) -> SummarizeBySegmentResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> SummarizeBySegmentResponse:
        return SummarizeBySegmentResponse.from_dict(json)

    def _create_body(
        self,
        source: str,
        source_type: str,
        focus: Optional[str],
    ) -> Dict[str, Any]:
        return {
            "source": source,
            "sourceType": source_type,
            "focus": focus,
        }
