from typing import Optional, List

from ai21.clients.sagemaker.resources.sagemaker_resource import SageMakerResource
from ai21.models import Penalty, CompletionsResponse


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
            "frequencyPenalty": None if frequency_penalty is None else frequency_penalty.to_dict(),
            "presencePenalty": None if presence_penalty is None else presence_penalty.to_dict(),
            "countPenalty": None if count_penalty is None else count_penalty.to_dict(),
        }
        raw_response = self._invoke(body)

        return CompletionsResponse.from_dict(raw_response)
