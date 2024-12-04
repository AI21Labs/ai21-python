from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from ai21.clients.common.beta.assistant.messages import BaseMessages
from ai21.models.assistant.message import Message
from ai21.models.responses.thread_response import ThreadResponse


class BaseThreads(ABC):
    _module_name = "threads"
    messages: BaseMessages

    @abstractmethod
    def create(
        self,
        messages: List[Message],
        **kwargs,
    ) -> ThreadResponse:
        pass

    @abstractmethod
    def retrieve(self, thread_id: str) -> ThreadResponse:
        pass
