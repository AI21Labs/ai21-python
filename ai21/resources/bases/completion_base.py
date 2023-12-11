from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any, overload

from ai21.resources.responses.completion_response import CompletionsResponse


class Completion(ABC):
    _module_name = "complete"

    @abstractmethod
    def create(
        self,
        model: str,
        prompt: str,
        *,
        max_tokens: int = 64,
        num_results: int = 1,
        min_tokens=0,
        temperature=0.7,
        top_p=1,
        top_k_return=0,
        custom_model: Optional[str] = None,
        experimental_mode: bool = False,
        stop_sequences: Optional[List[str]] = (),
        frequency_penalty: Optional[Dict[str, Any]] = {},
        presence_penalty: Optional[Dict[str, Any]] = {},
        count_penalty: Optional[Dict[str, Any]] = {},
        epoch: Optional[int] = None,
        **kwargs,
    ) -> CompletionsResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> CompletionsResponse:
        return CompletionsResponse.model_validate(json)


class AWSCompletionAdapter:
    @abstractmethod
    def create(
        self,
        model_id: str,
        prompt: str,
        max_tokens: int = 64,
        num_results: int = 1,
        min_tokens=0,
        temperature=0.7,
        top_p=1,
        top_k_return=0,
        stop_sequences: Optional[List[str]] = (),
        frequency_penalty: Optional[Dict[str, Any]] = {},
        presence_penalty: Optional[Dict[str, Any]] = {},
        count_penalty: Optional[Dict[str, Any]] = {},
    ) -> CompletionsResponse:
        pass
