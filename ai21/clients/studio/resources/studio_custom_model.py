from typing import List, Optional

from ai21.clients.common.custom_model_base import CustomModel
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import CustomBaseModelResponse


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
        body = self._create_body(
            dataset_id=dataset_id,
            model_name=model_name,
            model_type=model_type,
            learning_rate=learning_rate,
            num_epochs=num_epochs,
            **kwargs,
        )
        self._post(path=f"/{self._module_name}", body=body, response_cls=None)

    def list(self) -> List[CustomBaseModelResponse]:
        return self._get(path=f"/{self._module_name}", response_cls=List[CustomBaseModelResponse])

    def get(self, resource_id: str) -> CustomBaseModelResponse:
        return self._get(path=f"/{self._module_name}/{resource_id}", response_cls=CustomBaseModelResponse)


class AsyncStudioCustomModel(AsyncStudioResource, CustomModel):
    async def create(
        self,
        dataset_id: str,
        model_name: str,
        model_type: str,
        *,
        learning_rate: Optional[float] = None,
        num_epochs: Optional[int] = None,
        **kwargs,
    ) -> None:
        body = self._create_body(
            dataset_id=dataset_id,
            model_name=model_name,
            model_type=model_type,
            learning_rate=learning_rate,
            num_epochs=num_epochs,
            **kwargs,
        )
        await self._post(path=f"/{self._module_name}", body=body, response_cls=None)

    async def list(self) -> List[CustomBaseModelResponse]:
        return await self._get(path=f"/{self._module_name}", response_cls=List[CustomBaseModelResponse])

    async def get(self, resource_id: str) -> CustomBaseModelResponse:
        return await self._get(path=f"/{self._module_name}/{resource_id}", response_cls=CustomBaseModelResponse)
