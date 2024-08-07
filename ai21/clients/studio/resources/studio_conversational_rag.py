from __future__ import annotations
from typing import List

from ai21.clients.common.conversational_rag import ConversationalRag
from ai21.clients.studio.resources.studio_resource import (
    AsyncStudioResource,
    StudioResource,
)
from ai21.models.chat import ChatMessage
from ai21.models.responses.conversational_rag_response import ConversationalRagResponse
from ai21.models.retrieval_strategy import RetrievalStrategy
from ai21.types import NotGiven, NOT_GIVEN


class StudioConversationalRag(StudioResource, ConversationalRag):
    def create(
        self,
        messages: List[ChatMessage],
        *,
        path: str | NotGiven = NOT_GIVEN,
        labels: List[str] | NotGiven = NOT_GIVEN,
        file_ids: List[str] | NotGiven = NOT_GIVEN,
        max_segments: int | NotGiven = NOT_GIVEN,
        retrieval_strategy: RetrievalStrategy | str | NotGiven = NOT_GIVEN,
        retrieval_similarity_threshold: float | NotGiven = NOT_GIVEN,
        max_neighbors: int | NotGiven = NOT_GIVEN,
        hybrid_search_alpha: float | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> ConversationalRagResponse:
        body = self._create_body(
            messages=messages,
            path=path,
            labels=labels,
            file_ids=file_ids,
            max_segments=max_segments,
            retrieval_strategy=retrieval_strategy,
            retrieval_similarity_threshold=retrieval_similarity_threshold,
            max_neighbors=max_neighbors,
            hybrid_search_alpha=hybrid_search_alpha,
            **kwargs,
        )

        return self._post(path=f"/{self._module_name}", body=body, response_cls=ConversationalRagResponse)


class AsyncStudioConversationalRag(AsyncStudioResource, ConversationalRag):
    async def create(
        self,
        messages: List[ChatMessage],
        *,
        path: str | NotGiven = NOT_GIVEN,
        labels: List[str] | NotGiven = NOT_GIVEN,
        file_ids: List[str] | NotGiven = NOT_GIVEN,
        max_segments: int | NotGiven = NOT_GIVEN,
        retrieval_strategy: RetrievalStrategy | str | NotGiven = NOT_GIVEN,
        retrieval_similarity_threshold: float | NotGiven = NOT_GIVEN,
        max_neighbors: int | NotGiven = NOT_GIVEN,
        hybrid_search_alpha: float | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> ConversationalRagResponse:
        body = self._create_body(
            messages=messages,
            path=path,
            labels=labels,
            file_ids=file_ids,
            max_segments=max_segments,
            retrieval_strategy=retrieval_strategy,
            retrieval_similarity_threshold=retrieval_similarity_threshold,
            max_neighbors=max_neighbors,
            hybrid_search_alpha=hybrid_search_alpha,
            **kwargs,
        )

        return await self._post(path=f"/{self._module_name}", body=body, response_cls=ConversationalRagResponse)
