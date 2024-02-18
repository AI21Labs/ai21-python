from ai21.clients.common.answer_base import Answer
from ai21.clients.sagemaker.resources.sagemaker_resource import SageMakerResource
from ai21.models import AnswerResponse


class SageMakerAnswer(SageMakerResource, Answer):
    def create(
        self,
        context: str,
        question: str,
        **kwargs,
    ) -> AnswerResponse:
        body = self._create_body(context=context, question=question)
        response = self._invoke(body)

        return self._json_to_response(response)
