from abc import ABC, abstractmethod
from typing import Optional, Any, Dict

from ai21.models import DocumentType, SummarizeBySegmentResponse


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

    def _create_body(
        self,
        source: str,
        source_type: str,
        focus: Optional[str],
        **kwargs,
    ) -> Dict[str, Any]:
        return {
            "source": source,
            "sourceType": source_type,
            "focus": focus,
            **kwargs,
        }
