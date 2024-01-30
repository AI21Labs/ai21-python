from typing import List, Optional

from ai21.clients.common.chat_base import Chat
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models.chat_message import ChatMessage
from ai21.models.penalty import Penalty
from ai21.models.responses.chat_response import ChatResponse


class StudioChat(StudioResource, Chat):
    def create(
        self,
        model: str,
        messages: List[ChatMessage],
        system: str,
        *,
        num_results: Optional[int] = 1,
        temperature: Optional[float] = 0.7,
        max_tokens: Optional[int] = 300,
        min_tokens: Optional[int] = 0,
        top_p: Optional[float] = 1.0,
        top_k_return: Optional[int] = 0,
        stop_sequences: Optional[List[str]] = None,
        frequency_penalty: Optional[Penalty] = None,
        presence_penalty: Optional[Penalty] = None,
        count_penalty: Optional[Penalty] = None,
        **kwargs,
    ) -> ChatResponse:
        body = self._create_body(
            model=model,
            messages=messages,
            system=system,
            num_results=num_results,
            temperature=temperature,
            max_tokens=max_tokens,
            min_tokens=min_tokens,
            top_p=top_p,
            top_k_return=top_k_return,
            stop_sequences=stop_sequences,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            count_penalty=count_penalty,
        )
        url = f"{self._client.get_base_url()}/{model}/{self._module_name}"
        response = self._post(url=url, body=body)
        return self._json_to_response(response)
