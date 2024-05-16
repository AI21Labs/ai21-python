from ai21.clients.common.answer_base import Answer
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models import AnswerResponse


class StudioAnswer(StudioResource, Answer):
    def create(
        self,
        context: str,
        question: str,
        **kwargs,
    ) -> AnswerResponse:
        url = f"{self._client.get_base_url()}/{self._module_name}"

        body = self._create_body(context=context, question=question, **kwargs)

        response = self._post(url=url, body=body)

        return self._json_to_response(response)
