from typing import Optional

from ai21.resources.bases.answer_base import Answer
from ai21.resources.responses.answer_response import AnswerResponse
from ai21.resources.sagemaker_resource import SageMakerResource


class SageMakerAnswer(SageMakerResource, Answer):
    def create(
        self,
        context: str,
        question: str,
        *,
        answer_length: Optional[str] = None,
        mode: Optional[str] = None,
        **kwargs,
    ) -> AnswerResponse:
        params = {
            "context": context,
            "question": question,
            "answerLength": answer_length,
            "mode": mode,
        }
        response = self._invoke(params)

        return self._json_to_response(response)
