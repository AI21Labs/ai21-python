from typing import Optional

from ai21.clients.common.summarize_by_segment_base import SummarizeBySegment
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import SummarizeBySegmentResponse, DocumentType
from ai21.version_utils import V3_DEPRECATION_MESSAGE, deprecated


class StudioSummarizeBySegment(StudioResource, SummarizeBySegment):
    @deprecated(V3_DEPRECATION_MESSAGE)
    def create(
        self,
        source: str,
        source_type: DocumentType,
        *,
        focus: Optional[str] = None,
        **kwargs,
    ) -> SummarizeBySegmentResponse:
        body = self._create_body(
            source=source,
            source_type=source_type,
            focus=focus,
            **kwargs,
        )

        return self._post(path=f"/{self._module_name}", body=body, response_cls=SummarizeBySegmentResponse)


class AsyncStudioSummarizeBySegment(AsyncStudioResource, SummarizeBySegment):
    @deprecated(V3_DEPRECATION_MESSAGE)
    async def create(
        self,
        source: str,
        source_type: DocumentType,
        *,
        focus: Optional[str] = None,
        **kwargs,
    ) -> SummarizeBySegmentResponse:
        body = self._create_body(
            source=source,
            source_type=source_type,
            focus=focus,
            **kwargs,
        )

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=SummarizeBySegmentResponse)
