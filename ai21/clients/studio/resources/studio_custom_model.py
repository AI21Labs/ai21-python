from typing import List, Optional

from ai21.clients.common.custom_model_base import CustomModel
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import CustomBaseModelResponse
from ai21.version_utils import deprecated, V3_DEPRECATION_MESSAGE


class StudioCustomModel(StudioResource, CustomModel):
    @deprecated(V3_DEPRECATION_MESSAGE)
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

    @deprecated(V3_DEPRECATION_MESSAGE)
    def list(self) -> List[CustomBaseModelResponse]:
        return self._get(path=f"/{self._module_name}", response_cls=List[CustomBaseModelResponse])

    @deprecated(V3_DEPRECATION_MESSAGE)
    def get(self, resource_id: str) -> CustomBaseModelResponse:
        return self._get(path=f"/{self._module_name}/{resource_id}", response_cls=CustomBaseModelResponse)


class AsyncStudioCustomModel(AsyncStudioResource, CustomModel):
    @deprecated(V3_DEPRECATION_MESSAGE)
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

    @deprecated(V3_DEPRECATION_MESSAGE)
    async def list(self) -> List[CustomBaseModelResponse]:
        return await self._get(path=f"/{self._module_name}", response_cls=List[CustomBaseModelResponse])

    @deprecated(V3_DEPRECATION_MESSAGE)
    async def get(self, resource_id: str) -> CustomBaseModelResponse:
        return await self._get(path=f"/{self._module_name}/{resource_id}", response_cls=CustomBaseModelResponse)
