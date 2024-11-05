from __future__ import annotations

from typing import Optional

from ai21.clients.common.summarize_base import Summarize
from ai21.clients.sagemaker.resources.sagemaker_resource import SageMakerResource, AsyncSageMakerResource
from ai21.models import SummarizeResponse, SummaryMethod
from ai21.version_utils import V3_DEPRECATION_MESSAGE, deprecated


class SageMakerSummarize(SageMakerResource, Summarize):
    @deprecated(V3_DEPRECATION_MESSAGE)
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

        response = self._post(body)

        return self._json_to_response(response.json())


class AsyncSageMakerSummarize(AsyncSageMakerResource, Summarize):
    @deprecated(V3_DEPRECATION_MESSAGE)
    async def create(
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

        response = await self._post(body)

        return self._json_to_response(response.json())
