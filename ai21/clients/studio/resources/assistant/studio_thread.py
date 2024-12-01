from __future__ import annotations

from typing import List

from ai21.clients.common.assistant.threads import Threads
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models.assistant.message import Message
from ai21.models.responses.thread_response import Thread


class StudioThread(StudioResource, Threads):
    def create(self, messages: List[Message], **kwargs) -> Thread:
        body = dict(messages=messages)

        return self._post(path=f"/{self._module_name}", body=body, response_cls=Thread)

    def get(self, thread_id: str) -> Thread:
        return self._get(path=f"/{self._module_name}/{thread_id}", response_cls=Thread)


class AsyncStudioThread(AsyncStudioResource, Threads):
    async def create(self, messages: List[Message], **kwargs) -> Thread:
        body = dict(messages=messages)

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=Thread)

    async def get(self, thread_id: str) -> Thread:
        return await self._get(path=f"/{self._module_name}/{thread_id}", response_cls=Thread)
