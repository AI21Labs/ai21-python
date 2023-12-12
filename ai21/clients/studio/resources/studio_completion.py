from __future__ import annotations

from typing import Optional, Dict, Any, List

from ai21.resources.bases.completion_base import Completion
from ai21.resources.responses.completion_response import CompletionsResponse
from ai21.resources.studio_resource import StudioResource


class StudioCompletion(StudioResource, Completion):
    def create(
        self,
        model: str,
        prompt: str,
        *,
        max_tokens: Optional[int] = None,
        num_results: Optional[int] = 1,
        min_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[int] = None,
        top_k_return: Optional[int] = None,
        custom_model: Optional[str] = None,
        experimental_mode: bool = False,
        stop_sequences: Optional[List[str]] = None,
        frequency_penalty: Optional[Dict[str, Any]] = None,
        presence_penalty: Optional[Dict[str, Any]] = None,
        count_penalty: Optional[Dict[str, Any]] = None,
        epoch: Optional[int] = None,
        **kwargs,
    ) -> CompletionsResponse:
        if experimental_mode:
            model = f"experimental/{model}"

        url = f"{self._client.get_base_url()}/{model}"

        if custom_model is not None:
            url = f"{url}/{custom_model}"

        url = f"{url}/{self._module_name}"
        body = {
            "model": model,
            "customModel": custom_model,
            "experimentalModel": experimental_mode,
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
        return self._json_to_response(self._post(url=url, body=body))
