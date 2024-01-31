from typing import Optional

from ai21.clients.common.paraphrase_base import Paraphrase
from ai21.clients.sagemaker.resources.sagemaker_resource import SageMakerResource
from ai21.models import ParaphraseStyleType, ParaphraseResponse


class SageMakerParaphrase(SageMakerResource, Paraphrase):
    def create(
        self,
        text: str,
        *,
        style: Optional[ParaphraseStyleType] = None,
        start_index: Optional[int] = 0,
        end_index: Optional[int] = None,
        **kwargs,
    ) -> ParaphraseResponse:
        body = self._create_body(
            text=text,
            style=style,
            start_index=start_index,
            end_index=end_index,
        )
        response = self._invoke(body=body)

        return self._json_to_response(response)
