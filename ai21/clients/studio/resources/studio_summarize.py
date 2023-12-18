from typing import Optional

from ai21.resources.bases.summarize_base import Summarize
from ai21.resources.responses.summarize_response import SummarizeResponse
from ai21.resources.studio_resource import StudioResource


class StudioSummarize(StudioResource, Summarize):
    _module_name = "summarize"

    def create(
        self,
        source: str,
        source_type: str,
        *,
        focus: Optional[str] = None,
        summary_method: Optional[str] = None,
        **kwargs,
    ) -> SummarizeResponse:
        # Make a summarize request to the AI21 API. Returns the response either as a string or a AI21Summarize object.
        body = self._create_body(
            source=source,
            source_type=source_type,
            focus=focus,
            summary_method=summary_method,
        )
        url = f"{self._client.get_base_url()}/{self._module_name}"
        response = self._post(url=url, body=body)

        return self._json_to_response(response)
