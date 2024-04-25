from __future__ import annotations

from typing import List, Optional, Union, Any, Dict

from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models.chat import ChatMessage, ChatCompletionResponse
from ai21.models import ChatMessage as J2ChatMessage
from ai21.types import NotGiven, NOT_GIVEN
from ai21.utils.typing import remove_not_given

__all__ = ["ChatCompletions"]


class ChatCompletions(StudioResource):
    _module_name = "chat/completions"

    def create(
        self,
        model: str,
        messages: List[ChatMessage],
        max_tokens: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        stop: str | List[str] | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ChatCompletionResponse:
        if any(isinstance(item, J2ChatMessage) for item in messages):
            raise ValueError(
                "Please use the ChatMessage class from ai21.models.chat"
                " instead of ai21.models when working with chat completions."
            )

        body = self._create_body(
            model=model,
            messages=messages,
            stop=stop,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            n=n,
            **kwargs,
        )

        url = f"{self._client.get_base_url()}/{self._module_name}"
        response = self._post(url=url, body=body)
        return self._json_to_response(response)

    def _create_body(
        self,
        model: str,
        messages: List[ChatMessage],
        max_tokens: Optional[int] | NotGiven,
        temperature: Optional[float] | NotGiven,
        top_p: Optional[float] | NotGiven,
        stop: Optional[Union[str, List[str]]] | NotGiven,
        n: Optional[int] | NotGiven,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        return remove_not_given(
            {
                "model": model,
                "messages": [message.to_dict() for message in messages],
                "temperature": temperature,
                "maxTokens": max_tokens,
                "topP": top_p,
                "stop": stop,
                "n": n,
                **kwargs,
            }
        )

    def _json_to_response(self, json: Dict[str, Any]) -> ChatCompletionResponse:
        return ChatCompletionResponse.from_dict(json)
