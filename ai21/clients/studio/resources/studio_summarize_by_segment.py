from typing import Optional

from ai21.clients.common.summarize_by_segment_base import SummarizeBySegment
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models import SummarizeBySegmentResponse, DocumentType


class StudioSummarizeBySegment(StudioResource, SummarizeBySegment):
    def create(
        self, source: str, source_type: DocumentType, *, focus: Optional[str] = None, **kwargs
    ) -> SummarizeBySegmentResponse:
        body = self._create_body(
            source=source,
            source_type=source_type,
            focus=focus,
            **kwargs,
        )
        url = f"{self._client.get_base_url()}/{self._module_name}"

        return self._post(url=url, body=body, response_cls=SummarizeBySegmentResponse)
