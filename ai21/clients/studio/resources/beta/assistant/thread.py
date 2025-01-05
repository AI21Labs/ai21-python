from __future__ import annotations

from typing import List

from ai21.clients.common.beta.assistant.threads import BaseThreads
from ai21.clients.studio.resources.beta.assistant.thread_messages import ThreadMessages, AsyncThreadMessages
from ai21.clients.studio.resources.beta.assistant.thread_runs import AsyncThreadRuns, ThreadRuns
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models.assistant.message import Message, modify_message_content
from ai21.models.responses.thread_response import ThreadResponse


class Threads(StudioResource, BaseThreads):
    def __init__(self, client: AI21HTTPClient):
        super().__init__(client)

        self.messages = ThreadMessages(client)
        self.runs = ThreadRuns(client)

    def create(
        self,
        messages: List[Message],
        **kwargs,
    ) -> ThreadResponse:
        body = dict(messages=[modify_message_content(message) for message in messages])

        return self._post(path=f"/{self._module_name}", body=body, response_cls=ThreadResponse)

    def retrieve(self, thread_id: str) -> ThreadResponse:
        return self._get(path=f"/{self._module_name}/{thread_id}", response_cls=ThreadResponse)


class AsyncThreads(AsyncStudioResource, BaseThreads):
    def __init__(self, client: AsyncAI21HTTPClient):
        super().__init__(client)

        self.messages = AsyncThreadMessages(client)
        self.runs = AsyncThreadRuns(client)

    async def create(
        self,
        messages: List[Message],
        **kwargs,
    ) -> ThreadResponse:
        body = dict(messages=[modify_message_content(message) for message in messages])

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=ThreadResponse)

    async def retrieve(self, thread_id: str) -> ThreadResponse:
        return await self._get(path=f"/{self._module_name}/{thread_id}", response_cls=ThreadResponse)
