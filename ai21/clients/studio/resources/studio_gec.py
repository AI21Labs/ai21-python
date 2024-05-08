from ai21.clients.common.gec_base import GEC
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models import GECResponse


class StudioGEC(StudioResource, GEC):
    def create(self, text: str, **kwargs) -> GECResponse:
        body = self._create_body(text=text, **kwargs)
        url = f"{self._client.get_base_url()}/{self._module_name}"
        response = self._post(url=url, body=body)

        return self._json_to_response(response)
