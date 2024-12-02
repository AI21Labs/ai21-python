from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from ai21.clients.common.assistant.messages import Messages
from ai21.models.assistant.message import Message
from ai21.models.responses.thread_response import Thread


class Threads(ABC):
    _module_name = "threads"
    messages: Messages

    @abstractmethod
    def create(
        self,
        messages: List[Message],
        **kwargs,
    ) -> Thread:
        pass

    @abstractmethod
    def retrieve(self, thread_id: str) -> Thread:
        pass