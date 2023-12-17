from typing import Optional, List, Any, Dict

from ai21.resources.bedrock_resource import BedrockResource
from ai21.resources.responses.completion_response import CompletionsResponse


class BedrockCompletion(BedrockResource):
    def create(
        self,
        model_id: str,
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
            "frequencyPenalty": frequency_penalty or {},
            "presencePenalty": presence_penalty or {},
            "countPenalty": count_penalty or {},
        }
        raw_response = self._invoke(model_id=model_id, body=body)

        return CompletionsResponse.from_dict(raw_response)
