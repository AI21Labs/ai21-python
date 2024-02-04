from typing import Optional

from ai21.clients.common.answer_base import Answer
from ai21.clients.sagemaker.resources.sagemaker_resource import SageMakerResource
from ai21.models import AnswerResponse, AnswerLength, Mode


class SageMakerAnswer(SageMakerResource, Answer):
    def create(
        self,
        context: str,
        question: str,
        *,
        answer_length: Optional[AnswerLength] = None,
        mode: Optional[Mode] = None,
        **kwargs,
    ) -> AnswerResponse:
        body = self._create_body(context=context, question=question, answer_length=answer_length, mode=mode)
        response = self._invoke(body)

        return self._json_to_response(response)
