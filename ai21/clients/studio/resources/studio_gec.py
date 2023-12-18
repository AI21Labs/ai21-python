from ai21.resources.bases.gec_base import GEC
from ai21.resources.responses.gec_response import GECResponse
from ai21.resources.studio_resource import StudioResource


class StudioGEC(StudioResource, GEC):
    def create(self, text: str, **kwargs) -> GECResponse:
        body = self._create_body(text=text)
        url = f"{self._client.get_base_url()}/{self._module_name}"
        response = self._post(url=url, body=body)

        return self._json_to_response(response)
