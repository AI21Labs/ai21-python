from __future__ import annotations

from typing import List

from ai21.clients.common.assistant.thread import Thread
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models.responses.thread_response import CreateMessagePayload, ThreadResponse


class StudioThread(StudioResource, Thread):
    def create(
        self,
        messages: List[CreateMessagePayload],
        **kwargs,
    ) -> ThreadResponse:
        body = dict(messages=messages)

        return self._post(path=f"/{self._module_name}", body=body, response_cls=ThreadResponse)

    def get(self, thread_id: str) -> ThreadResponse:
        return self._get(path=f"/{self._module_name}/{thread_id}", response_cls=ThreadResponse)


class AsyncStudioThread(AsyncStudioResource, Thread):
    async def create(
        self,
        messages: List[CreateMessagePayload],
        **kwargs,
    ) -> ThreadResponse:
        body = dict(messages=messages)

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=ThreadResponse)

    async def get(self, thread_id: str) -> ThreadResponse:
        return await self._get(path=f"/{self._module_name}/{thread_id}", response_cls=ThreadResponse)
