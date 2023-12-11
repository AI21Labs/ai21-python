from __future__ import annotations

from typing import Optional

from ai21.resources.responses.summarize_response import SummarizeResponse
from ai21.resources.sagemaker_resource import SageMakerResource
from ai21.resources.bases.summarize_base import Summarize


class SageMakerSummarize(SageMakerResource, Summarize):
    def create(
        self,
        source: str,
        source_type: str,
        *,
        focus: Optional[str] = None,
        summary_method: Optional[str] = None,
        **kwargs,
    ) -> SummarizeResponse:
        params = {
            "source": source,
            "sourceType": source_type,
            "focus": focus,
            "summaryMethod": summary_method,
        }

        response = self._invoke(params)

        return self._json_to_response(response)
