from typing import Optional

from ai21.clients.common.summarize_base import Summarize
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import SummarizeResponse, SummaryMethod


class StudioSummarize(StudioResource, Summarize):
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
