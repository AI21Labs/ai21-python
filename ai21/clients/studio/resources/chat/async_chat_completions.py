from __future__ import annotations

from typing import List, Optional, Any, Literal, overload

from ai21.clients.studio.resources.studio_resource import AsyncStudioResource
from ai21.clients.studio.resources.chat.base_chat_completions import BaseChatCompletions
from ai21.models import ChatMessage as J2ChatMessage
from ai21.models.chat import ChatCompletionResponse, ChatCompletionChunk
from ai21.models.chat.chat_message import ChatMessageParam
from ai21.models.chat.document_schema import DocumentSchema
from ai21.models.chat.response_format import ResponseFormat
from ai21.models.chat.tool_defintions import ToolDefinition
from ai21.stream.async_stream import AsyncStream
from ai21.types import NotGiven, NOT_GIVEN

__all__ = ["AsyncChatCompletions"]


class AsyncChatCompletions(AsyncStudioResource, BaseChatCompletions):
    @overload
    async def create(
        self,
        model: str,
        messages: List[ChatMessageParam],
        max_tokens: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        stop: str | List[str] | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stream: Optional[False] | NotGiven = NOT_GIVEN,
        tools: List[ToolDefinition] | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        documents: List[DocumentSchema] | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ChatCompletionResponse:
        pass

    @overload
    async def create(
        self,
        model: str,
        messages: List[ChatMessageParam],
        stream: Literal[True],
        max_tokens: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        stop: str | List[str] | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        tools: List[ToolDefinition] | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        documents: List[DocumentSchema] | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> AsyncStream[ChatCompletionChunk]:
        pass

    async def create(
        self,
        model: str,
        messages: List[ChatMessageParam],
        max_tokens: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        stop: str | List[str] | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
        tools: List[ToolDefinition] | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        documents: List[DocumentSchema] | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ChatCompletionResponse | AsyncStream[ChatCompletionChunk]:
        if any(isinstance(item, J2ChatMessage) for item in messages):
            raise ValueError(
                "Please use the ChatMessage class from ai21.models.chat"
                " instead of ai21.models when working with chat completions."
            )

        body = self._create_body(
            model=self._get_model(model=model, model_id=kwargs.pop("model_id", None)),
            messages=messages,
            stop=stop,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            n=n,
            stream=stream or False,
            tools=tools,
            response_format=response_format,
            documents=documents,
            **kwargs,
        )

        return await self._post(
            path=f"/{self._module_name}",
            body=body,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionChunk],
            response_cls=ChatCompletionResponse,
        )
