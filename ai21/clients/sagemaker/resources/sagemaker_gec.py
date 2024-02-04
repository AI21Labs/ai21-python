from ai21.clients.common.gec_base import GEC
from ai21.clients.sagemaker.resources.sagemaker_resource import SageMakerResource
from ai21.models import GECResponse


class SageMakerGEC(SageMakerResource, GEC):
    def create(self, text: str, **kwargs) -> GECResponse:
        body = self._create_body(text=text)

        response = self._invoke(body)

        return self._json_to_response(response)
