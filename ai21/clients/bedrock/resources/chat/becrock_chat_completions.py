from __future__ import annotations
from typing import List, Any

from ai21.clients.bedrock.resources.bedrock_resource import BedrockResource
from ai21.models.chat import ChatMessage, ChatCompletionResponse
from ai21.types import NotGiven, NOT_GIVEN
from ai21.utils.typing import remove_not_given


class BedrockChatCompletions(BedrockResource):
    def create(
        self,
        messages: List[ChatMessage],
        *,
        max_tokens: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        stop: str | List[str] | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ChatCompletionResponse:
        body = remove_not_given(
            {
                "messages": [message.to_dict() for message in messages],
                "max_tokens": max_tokens,
                "temperature": temperature,
                "top_p": top_p,
                "stop": stop,
                "n": n,
            }
        )

        model_id = kwargs.get("model_id", self._model_id)

        if model_id is None:
            raise ValueError("model_id should be provided in either the constructor or the 'create' method call")

        raw_response = self._invoke(model_id=model_id, body=body)

        return ChatCompletionResponse.from_dict(raw_response)
