from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any

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
        stop_sequences: Optional[List[str]] = (),
        frequency_penalty: Optional[Dict[str, Any]] = {},
        presence_penalty: Optional[Dict[str, Any]] = {},
        count_penalty: Optional[Dict[str, Any]] = {},
        epoch: Optional[int] = None,
        **kwargs,
    ) -> CompletionsResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> CompletionsResponse:
        return CompletionsResponse.from_dict(json)

    def _create_body(
        self,
        model: str,
        prompt: str,
        max_tokens: Optional[int],
        num_results: Optional[int],
        min_tokens: Optional[int],
        temperature: Optional[float],
        top_p: Optional[int],
        top_k_return: Optional[int],
        custom_model: Optional[str],
        stop_sequences: Optional[List[str]],
        frequency_penalty: Optional[Dict[str, Any]],
        presence_penalty: Optional[Dict[str, Any]],
        count_penalty: Optional[Dict[str, Any]],
        epoch: Optional[int],
    ):
        return {
            "model": model,
            "customModel": custom_model,
            "prompt": prompt,
            "maxTokens": max_tokens,
            "numResults": num_results,
            "minTokens": min_tokens,
            "temperature": temperature,
            "topP": top_p,
            "topKReturn": top_k_return,
            "stopSequences": stop_sequences or [],
            "frequencyPenalty": frequency_penalty,
            "presencePenalty": presence_penalty,
            "countPenalty": count_penalty,
            "epoch": epoch,
        }
