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
        url = f"{self._client.get_base_url()}/{self._module_name}"

        body = self._create_body(context=context, question=question, answer_length=answer_length, mode=mode)

        response = self._post(url=url, body=body)

        return self._json_to_response(response)
