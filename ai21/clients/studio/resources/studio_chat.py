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
        # Make a chat request to the AI21 API. Returns the response either as a string or a AI21Chat object.
        params = {
            "model": model,
            "system": system,
            "messages": messages,
            "temperature": temperature,
            "maxTokens": max_tokens,
            "minTokens": min_tokens,
            "numResults": num_results,
            "topP": top_p,
            "topKReturn": top_k_returns,
            "stopSequences": stop_sequences,
            "frequencyPenalty": frequency_penalty,
            "presencePenalty": presence_penalty,
            "countPenalty": count_penalty,
        }
        url = f"{self._client.get_base_url()}/{model}/{self._module_name}"
        response = self._post(url=url, body=params)
        return self._json_to_response(response)
