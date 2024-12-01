from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from ai21.models.responses.thread_response import ThreadResponse, CreateMessagePayload


class Thread(ABC):
    _module_name = "threads"

    @abstractmethod
    def create(
        self,
        messages: List[CreateMessagePayload],
        **kwargs,
    ) -> ThreadResponse:
        pass

    @abstractmethod
    def get(self, thread_id: str) -> ThreadResponse:
        pass
