from __future__ import annotations

from abc import ABC, abstractmethod

from ai21.models.assistant.message import ThreadMessageRole, ThreadMessageContent
from ai21.models.responses.message_response import MessageResponse, ListMessageResponse


class BaseMessages(ABC):
    _module_name = "messages"

    @abstractmethod
    def create(
        self,
        thread_id: str,
        *,
        role: ThreadMessageRole,
        content: ThreadMessageContent,
        **kwargs,
    ) -> MessageResponse:
        pass

    @abstractmethod
    def list(self, thread_id: str) -> ListMessageResponse:
        pass
