from __future__ import annotations

from typing import List, Any, Optional

import boto3

from ai21.clients.bedrock.resources.bedrock_resource import BedrockResource
from ai21.clients.bedrock.resources.chat.becrock_chat_completions import BedrockChatCompletions
from ai21.http_client.http_client import HttpClient
from ai21.models.chat import ChatMessage, ChatCompletionResponse
from ai21.types import NotGiven, NOT_GIVEN


class BedrockChat(BedrockResource):
    def __init__(
        self,
        region: str,
        client: HttpClient,
        model_id: Optional[str] = None,
        aws_session: Optional[boto3.Session] = None,
    ):
        super().__init__(model_id=model_id, region=region, client=client, aws_session=aws_session)
        self._chat_completions = BedrockChatCompletions(
            model_id=model_id, region=region, client=client, aws_session=aws_session
        )

    @property
    def completions(self) -> BedrockChatCompletions:
        return self._chat_completions

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
        return self._chat_completions.create(
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stop=stop,
            n=n,
            **kwargs,
        )
