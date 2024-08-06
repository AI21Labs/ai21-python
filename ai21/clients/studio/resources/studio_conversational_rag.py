from ai21.clients.common.conversational_rag import ConversationalRag
from ai21.clients.studio.resources.studio_resource import (
    AsyncStudioResource,
    StudioResource,
)
from ai21.models import ChatMessage
from ai21.models.responses.conversational_rag_response import ConversationalRagResponse
from ai21.models.retrieval_strategy import RetrievalStrategy
from ai21.types import NotGiven


class StudioConversationalRag(StudioResource, ConversationalRag):
    def create(
        self,
        messages: list[ChatMessage],
        *,
        path: str | NotGiven = NotGiven,
        labels: list[str] | NotGiven = NotGiven,
        file_ids: list[str] | NotGiven = NotGiven,
        max_segments: int | NotGiven = NotGiven,
        retrieval_strategy: RetrievalStrategy | NotGiven = NotGiven,
        retrieval_similarity_threshold: float | NotGiven = NotGiven,
        max_neighbors: int | NotGiven = NotGiven,
        hybrid_search_alpha: float | NotGiven = NotGiven,
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

        return self._post(path=self._endpoint, body=body, response_cls=ConversationalRagResponse)


class AsyncStudioConversationalRag(AsyncStudioResource, ConversationalRag):
    async def create(
        self,
        messages: list[ChatMessage],
        *,
        path: str | NotGiven = NotGiven,
        labels: list[str] | NotGiven = NotGiven,
        file_ids: list[str] | NotGiven = NotGiven,
        max_segments: int | NotGiven = NotGiven,
        retrieval_strategy: RetrievalStrategy | NotGiven = NotGiven,
        retrieval_similarity_threshold: float | NotGiven = NotGiven,
        max_neighbors: int | NotGiven = NotGiven,
        hybrid_search_alpha: float | NotGiven = NotGiven,
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

        return await self._post(path=f"/{self._endpoint}", body=body, response_cls=ConversationalRagResponse)
