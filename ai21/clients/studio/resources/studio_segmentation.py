from ai21.resources.bases.segmentation_base import Segmentation
from ai21.resources.studio_resource import StudioResource


class StudioSegmentation(StudioResource, Segmentation):
    def create(self, source: str, source_type: str, **kwargs):
        body = self._create_body(source=source, source_type=source_type)
        url = f"{self._client.get_base_url()}/{self._module_name}"
        raw_response = self._post(url=url, body=body)

        return self._json_to_response(raw_response)
