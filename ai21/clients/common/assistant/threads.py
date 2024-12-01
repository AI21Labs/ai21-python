from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from ai21.models.assistant.thread_message import CreateThreadMessagePayload
from ai21.models.responses.thread_response import Thread


class Threads(ABC):
    _module_name = "threads"

    @abstractmethod
    def create(
        self,
        messages: List[CreateThreadMessagePayload],
        **kwargs,
    ) -> Thread:
        pass

    @abstractmethod
    def get(self, thread_id: str) -> Thread:
        pass
