from ai21.clients.common.segmentation_base import Segmentation
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models import DocumentType, SegmentationResponse


class StudioSegmentation(StudioResource, Segmentation):
    def create(self, source: str, source_type: DocumentType, **kwargs) -> SegmentationResponse:
        body = self._create_body(source=source, source_type=source_type.value, **kwargs)
        url = f"{self._client.get_base_url()}/{self._module_name}"

        return self._post(url=url, body=body, response_cls=SegmentationResponse)
