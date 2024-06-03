from typing import List

from ai21.clients.common.improvements_base import Improvements
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.errors import EmptyMandatoryListError
from ai21.models import ImprovementType, ImprovementsResponse


class StudioImprovements(StudioResource, Improvements):
    def create(self, text: str, types: List[ImprovementType], **kwargs) -> ImprovementsResponse:
        if len(types) == 0:
            raise EmptyMandatoryListError("types")

        url = f"{self._client.get_base_url()}/{self._module_name}"
        body = self._create_body(text=text, types=types, **kwargs)

        return self._post(url=url, body=body, response_cls=ImprovementsResponse)


class AsyncStudioImprovements(AsyncStudioResource, Improvements):
    async def create(self, text: str, types: List[ImprovementType], **kwargs) -> ImprovementsResponse:
        if len(types) == 0:
            raise EmptyMandatoryListError("types")

        url = f"{self._client.get_base_url()}/{self._module_name}"
        body = self._create_body(text=text, types=types, **kwargs)

        return await self._post(url=url, body=body, response_cls=ImprovementsResponse)
