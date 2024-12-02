from __future__ import annotations

from typing import List

from ai21.clients.common.assistant.threads import Threads
from ai21.clients.studio.resources.assistant.studio_thread_message import StudioThreadMessage, AsyncStudioThreadMessage
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models.assistant.message import Message
from ai21.models.responses.thread_response import Thread


class StudioThread(StudioResource, Threads):
    def __init__(self, client: AI21HTTPClient):
        super().__init__(client)

        self.messages = StudioThreadMessage(client)

    def create(
        self,
        messages: List[Message],
        **kwargs,
    ) -> Thread:
        body = dict(messages=messages)

        return self._post(path=f"/{self._module_name}", body=body, response_cls=Thread)

    def retrieve(self, thread_id: str) -> Thread:
        return self._get(path=f"/{self._module_name}/{thread_id}", response_cls=Thread)


class AsyncStudioThread(AsyncStudioResource, Threads):
    def __init__(self, client: AsyncAI21HTTPClient):
        super().__init__(client)

        self.messages = AsyncStudioThreadMessage(client)

    async def create(
        self,
        messages: List[Message],
        **kwargs,
    ) -> Thread:
        body = dict(messages=messages)

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=Thread)

    async def retrieve(self, thread_id: str) -> Thread:
        return await self._get(path=f"/{self._module_name}/{thread_id}", response_cls=Thread)
