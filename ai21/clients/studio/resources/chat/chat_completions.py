from __future__ import annotations

from typing import Any, List, Literal, Optional, overload

from ai21.clients.studio.resources.chat.base_chat_completions import BaseChatCompletions
from ai21.clients.studio.resources.studio_resource import StudioResource
from ai21.models import ChatMessage as J2ChatMessage
from ai21.models.chat import ChatCompletionChunk, ChatCompletionResponse
from ai21.models.chat.chat_message import ChatMessageParam
from ai21.models.chat.document_schema import DocumentSchema
from ai21.models.chat.response_format import ResponseFormat
from ai21.models.chat.tool_defintions import ToolDefinition
from ai21.stream.stream import Stream
from ai21.types import NOT_GIVEN, NotGiven


__all__ = ["ChatCompletions"]


class ChatCompletions(StudioResource, BaseChatCompletions):
    @overload
    def create(
        self,
        model: str,
        messages: List[ChatMessageParam],
        max_tokens: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        stop: str | List[str] | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        tools: List[ToolDefinition] | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        documents: List[DocumentSchema] | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ChatCompletionResponse:
        pass

    @overload
    def create(
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
    ) -> Stream[ChatCompletionChunk]:
        pass

    def create(
        self,
        messages: List[ChatMessageParam],
        model: str,
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
    ) -> ChatCompletionResponse | Stream[ChatCompletionChunk]:
        if any(isinstance(item, J2ChatMessage) for item in messages):
            raise ValueError(
                "Please use the ChatMessage class from ai21.models.chat"
                " instead of ai21.models when working with chat completions."
            )

        model = self._get_model(model=model)

        body = self._create_body(
            model=model,
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

        return self._post(
            path=f"/{self._module_name}",
            body=body,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
            response_cls=ChatCompletionResponse,
        )

    def _get_model(self, model: str) -> str:
        if self._client.__class__.__name__ == "AI21Client":
            return self._check_model(model=model)

        return model
