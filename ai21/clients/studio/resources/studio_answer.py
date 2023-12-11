from typing import Optional

from ai21.resources.bases.answer_base import Answer
from ai21.resources.responses.answer_response import AnswerResponse
from ai21.resources.studio_resource import StudioResource


class StudioAnswer(StudioResource, Answer):
    def create(
        self,
        context: str,
        question: str,
        *,
        answer_length: Optional[str] = None,
        mode: Optional[str] = None,
        **kwargs,
    ) -> AnswerResponse:
        url = self._client.get_base_url()
        url = f"{url}/{self._MODULE_NAME}"

        params = {
            "context": context,
            "question": question,
            "answerLength": answer_length,
            "mode": mode,
        }

        response = self._invoke(url=url, body=params)

        return self._json_to_response(response)
