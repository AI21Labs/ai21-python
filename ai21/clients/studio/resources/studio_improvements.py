from typing import List

from ai21.errors import EmptyMandatoryListException
from ai21.resources.bases.improvements_base import Improvements
from ai21.resources.responses.improvement_response import ImprovementsResponse
from ai21.resources.studio_resource import StudioResource


class StudioImprovements(StudioResource, Improvements):
    def create(self, text: str, types: List[str], **kwargs) -> ImprovementsResponse:
        if len(types) == 0:
            raise EmptyMandatoryListException("types")

        url = f"{self._client.get_base_url()}/{self._module_name}"

        response = self._invoke(url=url, body={"text": text, "types": types})

        return self._json_to_response(response)
