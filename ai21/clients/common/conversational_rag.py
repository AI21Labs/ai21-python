from abc import ABC, abstractmethod
from typing import Any, Dict, List

from ai21.models import ChatMessage
from ai21.models.responses.conversational_rag_response import ConversationalRagResponse
from ai21.models.retrieval_strategy import RetrievalStrategy
from ai21.types import NotGiven


class ConversationalRag(ABC):
    _endpoint = "/studio/v1/conversational-rag"

    @abstractmethod
    def create(
        self,
        messages: List[ChatMessage],
        *,
        path: str | NotGiven = NotGiven,
        labels: List[str] | NotGiven = NotGiven,
        file_ids: List[str] | NotGiven = NotGiven,
        max_segments: int | NotGiven = NotGiven,
        retrieval_strategy: RetrievalStrategy | NotGiven = NotGiven,
        retrieval_similarity_threshold: float | NotGiven = NotGiven,
        max_neighbors: int | NotGiven = NotGiven,
        hybrid_search_alpha: float | NotGiven = NotGiven,
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

    def _create_body(self, **kwargs) -> Dict[str, Any]:
        return {k: v for k, v in kwargs.items() if v is not NotGiven}
