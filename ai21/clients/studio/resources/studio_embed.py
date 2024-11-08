from typing import List, Optional

from ai21.clients.common.embed_base import Embed
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import EmbedType, EmbedResponse
from ai21.version_utils import V3_DEPRECATION_MESSAGE, deprecated


class StudioEmbed(StudioResource, Embed):
    @deprecated(V3_DEPRECATION_MESSAGE)
    def create(self, texts: List[str], type: Optional[EmbedType] = None, **kwargs) -> EmbedResponse:
        body = self._create_body(texts=texts, type=type, **kwargs)

        return self._post(path=f"/{self._module_name}", body=body, response_cls=EmbedResponse)


class AsyncStudioEmbed(AsyncStudioResource, Embed):
    @deprecated(V3_DEPRECATION_MESSAGE)
    async def create(self, texts: List[str], type: Optional[EmbedType] = None, **kwargs) -> EmbedResponse:
        body = self._create_body(texts=texts, type=type, **kwargs)

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=EmbedResponse)
