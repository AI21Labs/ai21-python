from typing import Optional

from ai21.clients.common.summarize_base import Summarize
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models.responses.summarize_response import SummarizeResponse
from ai21.models.summary_method import SummaryMethod


class StudioSummarize(StudioResource, Summarize):
    _module_name = "summarize"

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
        url = f"{self._client.get_base_url()}/{self._module_name}"
        response = self._post(url=url, body=body)

        return self._json_to_response(response)
