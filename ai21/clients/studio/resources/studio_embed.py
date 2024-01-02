from typing import List, Optional

from ai21.resources.bases.embed_base import Embed
from ai21.models.responses import EmbedResponse
from ai21.resources.studio_resource import StudioResource


class StudioEmbed(StudioResource, Embed):
    def create(self, texts: List[str], type: Optional[str] = None, **kwargs) -> EmbedResponse:
        url = f"{self._client.get_base_url()}/{self._module_name}"
        body = self._create_body(texts=texts, type=type)
        response = self._post(url=url, body=body)

        return self._json_to_response(response)
