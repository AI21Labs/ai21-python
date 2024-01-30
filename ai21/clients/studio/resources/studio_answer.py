from typing import Optional

from ai21.clients.common.answer_base import Answer
from ai21.models import AnswerLength, Mode
from ai21.models.responses.answer_response import AnswerResponse
from ai21.clients.studio.resources.studio_resource import StudioResource


class StudioAnswer(StudioResource, Answer):
    def create(
        self,
        context: str,
        question: str,
        *,
        answer_length: Optional[AnswerLength] = None,
        mode: Optional[Mode] = None,
        **kwargs,
    ) -> AnswerResponse:
        url = f"{self._client.get_base_url()}/{self._module_name}"

        body = self._create_body(context=context, question=question, answer_length=answer_length, mode=mode)

        response = self._post(url=url, body=body)

        return self._json_to_response(response)
