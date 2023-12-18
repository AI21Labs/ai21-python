from typing import Optional

from ai21.resources.responses.summarize_by_segment_response import (
    SummarizeBySegmentResponse,
)
from ai21.resources.studio_resource import StudioResource
from ai21.resources.bases.summarize_by_segment_base import SummarizeBySegment


class StudioSummarizeBySegment(StudioResource, SummarizeBySegment):
    def create(
        self, source: str, source_type: str, *, focus: Optional[str] = None, **kwargs
    ) -> SummarizeBySegmentResponse:
        body = self._create_body(
            source=source,
            source_type=source_type,
            focus=focus,
        )
        url = f"{self._client.get_base_url()}/{self._module_name}"
        response = self._post(url=url, body=body)
        return self._json_to_response(response)
