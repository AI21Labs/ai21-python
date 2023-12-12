from typing import Optional

from ai21.resources.bases.paraphrase_base import Paraphrase
from ai21.resources.responses.paraphrase_response import ParaphraseResponse
from ai21.resources.studio_resource import StudioResource


class StudioParaphrase(StudioResource, Paraphrase):
    def create(
        self,
        text: str,
        *,
        style: Optional[str] = None,
        start_index: Optional[int] = None,
        end_index: Optional[int] = None,
        **kwargs,
    ) -> ParaphraseResponse:
        body = {
            "text": text,
            "style": style,
            "startIndex": start_index,
            "endIndex": end_index,
        }
        url = f"{self._client.get_base_url()}/{self._module_name}"
        response = self._post(url=url, body=body)

        return self._json_to_response(response)
