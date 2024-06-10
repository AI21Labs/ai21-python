from ai21.clients.common.segmentation_base import Segmentation
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import DocumentType, SegmentationResponse


class StudioSegmentation(StudioResource, Segmentation):
    def create(self, source: str, source_type: DocumentType, **kwargs) -> SegmentationResponse:
        body = self._create_body(source=source, source_type=source_type.value, **kwargs)

        return self._post(path=f"/{self._module_name}", body=body, response_cls=SegmentationResponse)


class AsyncStudioSegmentation(AsyncStudioResource, Segmentation):
    async def create(self, source: str, source_type: DocumentType, **kwargs) -> SegmentationResponse:
        body = self._create_body(source=source, source_type=source_type.value, **kwargs)

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=SegmentationResponse)
