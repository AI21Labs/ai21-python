from ai21.clients.common.gec_base import GEC
from ai21.clients.sagemaker.resources.sagemaker_resource import SageMakerResource, AsyncSageMakerResource
from ai21.models import GECResponse
from ai21.version_utils import V3_DEPRECATION_MESSAGE, deprecated


class SageMakerGEC(SageMakerResource, GEC):
    @deprecated(V3_DEPRECATION_MESSAGE)
    def create(self, text: str, **kwargs) -> GECResponse:
        body = self._create_body(text=text)

        response = self._post(body)

        return self._json_to_response(response.json())


class AsyncSageMakerGEC(AsyncSageMakerResource, GEC):
    @deprecated(V3_DEPRECATION_MESSAGE)
    async def create(self, text: str, **kwargs) -> GECResponse:
        body = self._create_body(text=text)

        response = await self._post(body)

        return self._json_to_response(response.json())
