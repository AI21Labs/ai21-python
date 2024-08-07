from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, List

from ai21.models.chat import ChatMessage
from ai21.models._pydantic_compatibility import _to_dict
from ai21.models.responses.conversational_rag_response import ConversationalRagResponse
from ai21.models.retrieval_strategy import RetrievalStrategy
from ai21.types import NotGiven, NOT_GIVEN
from ai21.utils.typing import remove_not_given


class ConversationalRag(ABC):
    _module_name = "conversational-rag"

    @abstractmethod
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
        """
        :param messages: List of ChatMessage objects.
        :param path: Search only files in the specified path or a child path.
        :param labels: Search only files with one of these labels.
        :param file_ids: List of file IDs to filter the sources by.
        :param max_segments: Maximum number of segments to retrieve.
        :param retrieval_strategy: The retrieval strategy to use.
        :param retrieval_similarity_threshold: The similarity threshold to use for retrieval.
        :param max_neighbors: Maximum number of neighbors to retrieve.
        :param hybrid_search_alpha: The alpha value to use for hybrid search.
        :param kwargs: Additional keyword arguments.
        :return: The response object.
        """
        pass

    def _create_body(
        self,
        messages: List[ChatMessage],
        *,
        path: str | NotGiven,
        labels: List[str] | NotGiven,
        file_ids: List[str] | NotGiven,
        max_segments: int | NotGiven,
        retrieval_strategy: RetrievalStrategy | str | NotGiven,
        retrieval_similarity_threshold: float | NotGiven,
        max_neighbors: int | NotGiven,
        hybrid_search_alpha: float | NotGiven,
        **kwargs,
    ) -> Dict[str, Any]:
        return remove_not_given(
            {
                "messages": [_to_dict(message) for message in messages],
                "path": path,
                "labels": labels,
                "file_ids": file_ids,
                "max_segments": max_segments,
                "retrieval_strategy": retrieval_strategy,
                "retrieval_similarity_threshold": retrieval_similarity_threshold,
                "max_neighbors": max_neighbors,
                "hybrid_search_alpha": hybrid_search_alpha,
                **kwargs,
            }
        )
