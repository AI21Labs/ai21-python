from ai21.clients.common.gec_base import GEC
from ai21.clients.sagemaker.resources.sagemaker_resource import SageMakerResource, AsyncSageMakerResource
from ai21.models import GECResponse


class SageMakerGEC(SageMakerResource, GEC):
    def create(self, text: str, **kwargs) -> GECResponse:
        body = self._create_body(text=text)

        response = self._post(body)

        return self._json_to_response(response.json())


class AsyncSageMakerGEC(AsyncSageMakerResource, GEC):
    async def create(self, text: str, **kwargs) -> GECResponse:
        body = self._create_body(text=text)

        response = await self._post(body)

        return self._json_to_response(response.json())
