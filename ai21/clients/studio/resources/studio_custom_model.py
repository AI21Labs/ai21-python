from typing import List, Optional

from ai21.clients.common.custom_model_base import CustomModel
from ai21.models.responses.custom_model_response import CustomBaseModelResponse
from ai21.clients.studio.resources.studio_resource import StudioResource


class StudioCustomModel(StudioResource, CustomModel):
    def create(
        self,
        dataset_id: str,
        model_name: str,
        model_type: str,
        *,
        learning_rate: Optional[float] = None,
        num_epochs: Optional[int] = None,
        **kwargs,
    ) -> None:
        url = f"{self._client.get_base_url()}/{self._module_name}"
        body = self._create_body(
            dataset_id=dataset_id,
            model_name=model_name,
            model_type=model_type,
            learning_rate=learning_rate,
            num_epochs=num_epochs,
        )
        self._post(url=url, body=body)

    def list(self) -> List[CustomBaseModelResponse]:
        url = f"{self._client.get_base_url()}/{self._module_name}"
        response = self._get(url=url)

        return [self._json_to_response(r) for r in response]

    def get(self, resource_id: str) -> CustomBaseModelResponse:
        url = f"{self._client.get_base_url()}/{self._module_name}/{resource_id}"
        return self._json_to_response(self._get(url=url))
