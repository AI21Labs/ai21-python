from typing import Optional

from ai21.resources.bases.paraphrase_base import Paraphrase
from ai21.resources.responses.paraphrase_response import ParaphraseResponse
from ai21.resources.sagemaker_resource import SageMakerResource


class SageMakerParaphrase(SageMakerResource, Paraphrase):
    def create(
        self,
        text: str,
        *,
        style: Optional[str] = None,
        start_index: Optional[int] = 0,
        end_index: Optional[int] = None,
        **kwargs,
    ) -> ParaphraseResponse:
        body = {
            "text": text,
            "style": style,
            "startIndex": start_index,
            "endIndex": end_index,
        }
        response = self._invoke(body=body)

        return self._json_to_response(response)
