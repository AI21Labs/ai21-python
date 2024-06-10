from ai21.clients.common.answer_base import Answer
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import AnswerResponse


class StudioAnswer(StudioResource, Answer):
    def create(
        self,
        context: str,
        question: str,
        **kwargs,
    ) -> AnswerResponse:
        body = self._create_body(context=context, question=question, **kwargs)

        return self._post(path=f"/{self._module_name}", body=body, response_cls=AnswerResponse)


class AsyncStudioAnswer(AsyncStudioResource, Answer):
    async def create(
        self,
        context: str,
        question: str,
        **kwargs,
    ) -> AnswerResponse:
        body = self._create_body(context=context, question=question, **kwargs)

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=AnswerResponse)
