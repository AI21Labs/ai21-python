from ai21.clients.common.gec_base import GEC
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models import GECResponse


class StudioGEC(StudioResource, GEC):
    def create(self, text: str, **kwargs) -> GECResponse:
        body = self._create_body(text=text, **kwargs)

        return self._post(path=f"/{self._module_name}", body=body, response_cls=GECResponse)
