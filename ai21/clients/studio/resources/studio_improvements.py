from typing import List

from ai21.clients.common.improvements_base import Improvements
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import ImprovementType, ImprovementsResponse
from ai21.version_utils import V3_DEPRECATION_MESSAGE, deprecated


class StudioImprovements(StudioResource, Improvements):
    @deprecated(V3_DEPRECATION_MESSAGE)
    def create(self, text: str, types: List[ImprovementType], **kwargs) -> ImprovementsResponse:
        self._validate_types(types)

        body = self._create_body(text=text, types=types, **kwargs)

        return self._post(path=f"/{self._module_name}", body=body, response_cls=ImprovementsResponse)


class AsyncStudioImprovements(AsyncStudioResource, Improvements):
    @deprecated(V3_DEPRECATION_MESSAGE)
    async def create(self, text: str, types: List[ImprovementType], **kwargs) -> ImprovementsResponse:
        self._validate_types(types)

        body = self._create_body(text=text, types=types, **kwargs)

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=ImprovementsResponse)
