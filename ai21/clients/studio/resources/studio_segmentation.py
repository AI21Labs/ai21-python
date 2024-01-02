from ai21.clients.common.segmentation_base import Segmentation
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models.document_type import DocumentType
from ai21.models.responses.segmentation_response import SegmentationResponse


class StudioSegmentation(StudioResource, Segmentation):
    def create(self, source: str, source_type: DocumentType, **kwargs) -> SegmentationResponse:
        body = self._create_body(source=source, source_type=source_type)
        url = f"{self._client.get_base_url()}/{self._module_name}"
        raw_response = self._post(url=url, body=body)

        return self._json_to_response(raw_response)
