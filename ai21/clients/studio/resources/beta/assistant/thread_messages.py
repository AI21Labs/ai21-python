from __future__ import annotations


from ai21.clients.common.beta.assistant.messages import BaseMessages
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models.assistant.message import ThreadMessageRole, modify_message_content, Message, ThreadMessageContent
from ai21.models.responses.message_response import MessageResponse, ListMessageResponse


class ThreadMessages(StudioResource, BaseMessages):
    def create(
        self,
        thread_id: str,
        *,
        role: ThreadMessageRole,
        content: ThreadMessageContent,
        **kwargs,
    ) -> MessageResponse:
        body = modify_message_content(Message(role=role, content=content))

        return self._post(path=f"/threads/{thread_id}/{self._module_name}", body=body, response_cls=MessageResponse)

    def list(self, thread_id: str) -> ListMessageResponse:
        return self._get(path=f"/threads/{thread_id}/{self._module_name}", response_cls=ListMessageResponse)


class AsyncThreadMessages(AsyncStudioResource, BaseMessages):
    async def create(
        self,
        thread_id: str,
        *,
        role: ThreadMessageRole,
        content: ThreadMessageContent,
        **kwargs,
    ) -> MessageResponse:
        body = modify_message_content(Message(role=role, content=content))

        return await self._post(
            path=f"/threads/{thread_id}/{self._module_name}", body=body, response_cls=MessageResponse
        )

    async def list(self, thread_id: str) -> ListMessageResponse:
        return await self._get(path=f"/threads/{thread_id}/{self._module_name}", response_cls=ListMessageResponse)
