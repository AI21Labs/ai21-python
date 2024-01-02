from __future__ import annotations

from typing import Optional

from ai21.resources.bases.summarize_base import Summarize
from ai21.models.summary_method import SummaryMethod
from ai21.models.responses import SummarizeResponse
from ai21.resources.sagemaker_resource import SageMakerResource


class SageMakerSummarize(SageMakerResource, Summarize):
    def create(
        self,
        source: str,
        source_type: str,
        *,
        focus: Optional[str] = None,
        summary_method: Optional[SummaryMethod] = None,
        **kwargs,
    ) -> SummarizeResponse:
        body = self._create_body(
            source=source,
            source_type=source_type,
            focus=focus,
            summary_method=summary_method,
        )

        response = self._invoke(body)

        return self._json_to_response(response)
