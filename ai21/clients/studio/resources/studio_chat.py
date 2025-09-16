from __future__ import annotations

from typing import List, Optional

from ai21.clients.common.chat_base import Chat
from ai21.clients.studio.resources.chat import ChatCompletions, AsyncChatCompletions
from ai21.models.chat import ChatMessage as JambaChatMessage
from ai21.clients.studio.resources.studio_resource import StudioResource, AsyncStudioResource
from ai21.models import ChatMessage, Penalty, ChatResponse
from ai21.types import NotGiven, NOT_GIVEN
from ai21.clients.studio.resources.constants import (
    CHAT_DEFAULT_NUM_RESULTS,
    CHAT_DEFAULT_TEMPERATURE,
    CHAT_DEFAULT_MAX_TOKENS,
    CHAT_DEFAULT_MIN_TOKENS,
    CHAT_DEFAULT_TOP_P,
    CHAT_DEFAULT_TOP_K_RETURN,
)


class StudioChat(StudioResource, Chat):
    def create(
        self,
        model: str,
        messages: List[ChatMessage],
        system: str,
        *,
        num_results: Optional[int] = CHAT_DEFAULT_NUM_RESULTS,
        temperature: Optional[float] = CHAT_DEFAULT_TEMPERATURE,
        max_tokens: Optional[int] = CHAT_DEFAULT_MAX_TOKENS,
        min_tokens: Optional[int] = CHAT_DEFAULT_MIN_TOKENS,
        top_p: Optional[float] = CHAT_DEFAULT_TOP_P,
        top_k_return: Optional[int] = CHAT_DEFAULT_TOP_K_RETURN,
        stop_sequences: Optional[List[str]] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[Penalty] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[Penalty] | NotGiven = NOT_GIVEN,
        count_penalty: Optional[Penalty] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> ChatResponse:
        if any(isinstance(item, JambaChatMessage) for item in messages):
            raise ValueError(
                "Please use the ChatMessage class from ai21.models"
                " instead of ai21.models.chat when working with chat"
            )

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
            **kwargs,
        )

        return self._post(path=f"/{model}/{self._module_name}", body=body, response_cls=ChatResponse)

    @property
    def completions(self) -> ChatCompletions:
        return ChatCompletions(self._client)


class AsyncStudioChat(AsyncStudioResource, Chat):
    async def create(
        self,
        model: str,
        messages: List[ChatMessage],
        system: str,
        *,
        num_results: Optional[int] = CHAT_DEFAULT_NUM_RESULTS,
        temperature: Optional[float] = CHAT_DEFAULT_TEMPERATURE,
        max_tokens: Optional[int] = CHAT_DEFAULT_MAX_TOKENS,
        min_tokens: Optional[int] = CHAT_DEFAULT_MIN_TOKENS,
        top_p: Optional[float] = CHAT_DEFAULT_TOP_P,
        top_k_return: Optional[int] = CHAT_DEFAULT_TOP_K_RETURN,
        stop_sequences: Optional[List[str]] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[Penalty] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[Penalty] | NotGiven = NOT_GIVEN,
        count_penalty: Optional[Penalty] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> ChatResponse:
        if any(isinstance(item, JambaChatMessage) for item in messages):
            raise ValueError(
                "Please use the ChatMessage class from ai21.models"
                " instead of ai21.models.chat when working with chat"
            )

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
            **kwargs,
        )
        return await self._post(path=f"/{model}/{self._module_name}", body=body, response_cls=ChatResponse)

    @property
    def completions(self) -> AsyncChatCompletions:
        return AsyncChatCompletions(self._client)
