from typing import Optional

from ai21.clients.common.summarize_base import Summarize
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import SummarizeResponse, SummaryMethod
from ai21.version_utils import V3_DEPRECATION_MESSAGE, deprecated


class StudioSummarize(StudioResource, Summarize):
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
            **kwargs,
        )

        return self._post(path=f"/{self._module_name}", body=body, response_cls=SummarizeResponse)


class AsyncStudioSummarize(AsyncStudioResource, Summarize):
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
            **kwargs,
        )

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=SummarizeResponse)
