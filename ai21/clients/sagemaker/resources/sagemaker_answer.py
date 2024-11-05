from ai21.clients.common.answer_base import Answer
from ai21.clients.sagemaker.resources.sagemaker_resource import SageMakerResource, AsyncSageMakerResource
from ai21.models import AnswerResponse
from ai21.version_utils import V3_DEPRECATION_MESSAGE, deprecated


class SageMakerAnswer(SageMakerResource, Answer):
    @deprecated(V3_DEPRECATION_MESSAGE)
    def create(
        self,
        context: str,
        question: str,
        **kwargs,
    ) -> AnswerResponse:
        body = self._create_body(context=context, question=question)
        response = self._post(body)

        return self._json_to_response(response.json())


class AsyncSageMakerAnswer(AsyncSageMakerResource, Answer):
    @deprecated(V3_DEPRECATION_MESSAGE)
    async def create(
        self,
        context: str,
        question: str,
        **kwargs,
    ) -> AnswerResponse:
        body = self._create_body(context=context, question=question)
        response = await self._post(body)

        return self._json_to_response(response.json())
