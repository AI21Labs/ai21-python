from abc import ABC, abstractmethod
from typing import Optional, Any, Dict

from ai21.resources.responses.summarize_response import SummarizeResponse


class Summarize(ABC):
    @abstractmethod
    def create(
        self,
        source: str,
        source_type: str,
        *,
        focus: Optional[str] = None,
        summary_method: Optional[str] = None,
        **kwargs,
    ) -> SummarizeResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> SummarizeResponse:
        return SummarizeResponse.from_dict(json)

    def _create_body(
        self,
        source: str,
        source_type: str,
        focus: Optional[str],
        summary_method: Optional[str],
    ) -> Dict[str, Any]:
        return {
            "source": source,
            "sourceType": source_type,
            "focus": focus,
            "summaryMethod": summary_method,
        }
