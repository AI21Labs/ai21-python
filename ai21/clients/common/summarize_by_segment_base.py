from abc import ABC, abstractmethod
from typing import Optional, Any, Dict

from ai21.models.document_type import DocumentType
from ai21.models.responses.summarize_by_segment_response import (
    SummarizeBySegmentResponse,
)


class SummarizeBySegment(ABC):
    _module_name = "summarize-by-segment"

    @abstractmethod
    def create(
        self,
        source: str,
        source_type: DocumentType,
        *,
        focus: Optional[str] = None,
        **kwargs,
    ) -> SummarizeBySegmentResponse:
        """

        :param source: The input text, or URL of a web page to be summarized.
        :param source_type: Either TEXT or URL
        :param focus: Summaries focused on a topic of your choice.
        :param kwargs:
        :return:
        """
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
