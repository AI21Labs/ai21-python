from ai21.clients.common.gec_base import GEC
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import GECResponse
from ai21.version_utils import V3_DEPRECATION_MESSAGE, deprecated


class StudioGEC(StudioResource, GEC):
    @deprecated(V3_DEPRECATION_MESSAGE)
    def create(self, text: str, **kwargs) -> GECResponse:
        body = self._create_body(text=text, **kwargs)

        return self._post(path=f"/{self._module_name}", body=body, response_cls=GECResponse)


class AsyncStudioGEC(AsyncStudioResource, GEC):
    @deprecated(V3_DEPRECATION_MESSAGE)
    async def create(self, text: str, **kwargs) -> GECResponse:
        body = self._create_body(text=text, **kwargs)

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=GECResponse)
