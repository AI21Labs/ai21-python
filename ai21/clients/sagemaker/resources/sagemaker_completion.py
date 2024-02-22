from typing import Optional, List

from ai21.clients.sagemaker.resources.sagemaker_resource import SageMakerResource
from ai21.models import Penalty, CompletionsResponse


class SageMakerCompletion(SageMakerResource):
    def create(
        self,
        prompt: str,
        *,
        max_tokens: int = 64,
        num_results: int = 1,
        min_tokens: int = 0,
        temperature: float = 0.7,
        top_p: float = 1,
        top_k_return: int = 0,
        stop_sequences: Optional[List[str]] = None,
        frequency_penalty: Optional[Penalty] = None,
        presence_penalty: Optional[Penalty] = None,
        count_penalty: Optional[Penalty] = None,
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
        }

        if frequency_penalty is not None:
            body["frequencyPenalty"] = frequency_penalty.to_dict()

        if presence_penalty is not None:
            body["presencePenalty"] = presence_penalty.to_dict()

        if count_penalty is not None:
            body["countPenalty"] = count_penalty.to_dict()

        raw_response = self._invoke(body)

        return CompletionsResponse.from_dict(raw_response)
