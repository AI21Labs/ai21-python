from typing import List, Optional

from ai21.clients.common.embed_base import Embed
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models.embed_type import EmbedType
from ai21.models.responses.embed_response import EmbedResponse


class StudioEmbed(StudioResource, Embed):
    def create(self, texts: List[str], type: Optional[EmbedType] = None, **kwargs) -> EmbedResponse:
        url = f"{self._client.get_base_url()}/{self._module_name}"
        body = self._create_body(texts=texts, type=type)
        response = self._post(url=url, body=body)

        return self._json_to_response(response)
