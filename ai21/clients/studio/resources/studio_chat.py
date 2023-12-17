from typing import List, Any, Optional, Dict

from ai21.resources.bases.chat_base import Chat, Message
from ai21.resources.responses.chat_response import ChatResponse
from ai21.resources.studio_resource import StudioResource


class StudioChat(StudioResource, Chat):
    def create(
        self,
        model: str,
        messages: List[Message],
        system: str,
        *,
        num_results: Optional[int] = 1,
        temperature: Optional[float] = 0.7,
        max_tokens: Optional[int] = 300,
        min_tokens: Optional[int] = 0,
        top_p: Optional[float] = 1.0,
        top_k_returns: Optional[int] = 0,
        stop_sequences: Optional[List[str]] = None,
        frequency_penalty: Optional[Dict[str, Any]] = None,
        presence_penalty: Optional[Dict[str, Any]] = None,
        count_penalty: Optional[Dict[str, Any]] = None,
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
            top_k_returns=top_k_returns,
            stop_sequences=stop_sequences,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            count_penalty=count_penalty,
        )
        url = f"{self._client.get_base_url()}/{model}/{self._module_name}"
        response = self._post(url=url, body=body)
        return self._json_to_response(response)
