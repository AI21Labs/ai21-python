from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional

from ai21.clients.common.beta.assistant.messages import BaseMessages
from ai21.models.assistant.message import Message, modify_message_content
from ai21.models.responses.thread_response import ThreadResponse
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class BaseThreads(ABC):
    _module_name = "threads"
    messages: BaseMessages

    @abstractmethod
    def create(
        self,
        messages: List[Message] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> ThreadResponse:
        pass

    def _create_body(self, messages: List[Message] | NotGiven, **kwargs) -> Optional[dict]:
        body = remove_not_given({"messages": messages, **kwargs})

        body["messages"] = [modify_message_content(message) for message in body.get("messages", [])]

        return body

    @abstractmethod
    def retrieve(self, thread_id: str) -> ThreadResponse:
        pass
