from typing import Optional, Dict, Any, List

from ai21.resources.responses.completion_response import CompletionsResponse
from ai21.resources.sagemaker_resource import SageMakerResource


class SageMakerCompletion(SageMakerResource):
    def create(
        self,
        prompt: str,
        *,
        max_tokens: Optional[int] = None,
        num_results: Optional[int] = 1,
        min_tokens: Optional[int] = 0,
        temperature: Optional[float] = 0.7,
        top_p: Optional[int] = 1,
        top_k_return: Optional[int] = 0,
        stop_sequences: Optional[List[str]] = None,
        frequency_penalty: Optional[Dict[str, Any]] = None,
        presence_penalty: Optional[Dict[str, Any]] = None,
        count_penalty: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> CompletionsResponse:
        body = {
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
        }
        raw_response = self._invoke(body)

        return CompletionsResponse.from_dict(raw_response)
