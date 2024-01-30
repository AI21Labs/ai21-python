from typing import List

from ai21.clients.common.improvements_base import Improvements
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.errors import EmptyMandatoryListError
from ai21.models import ImprovementType
from ai21.models.responses.improvement_response import ImprovementsResponse


class StudioImprovements(StudioResource, Improvements):
    def create(self, text: str, types: List[ImprovementType], **kwargs) -> ImprovementsResponse:
        if len(types) == 0:
            raise EmptyMandatoryListError("types")

        url = f"{self._client.get_base_url()}/{self._module_name}"
        body = self._create_body(text=text, types=types)
        response = self._post(url=url, body=body)

        return self._json_to_response(response)
