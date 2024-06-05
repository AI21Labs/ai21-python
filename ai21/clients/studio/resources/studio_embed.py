from typing import List, Optional

from ai21.clients.common.embed_base import Embed
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models import EmbedType, EmbedResponse


class StudioEmbed(StudioResource, Embed):
    def create(self, texts: List[str], type: Optional[EmbedType] = None, **kwargs) -> EmbedResponse:
        url = self._client.get_base_url(module_name=self._module_name)
        body = self._create_body(texts=texts, type=type, **kwargs)

        return self._post(url=url, body=body, response_cls=EmbedResponse)
