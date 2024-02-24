from __future__ import annotations

from typing import List

from ai21.clients.bedrock.resources.bedrock_resource import BedrockResource
from ai21.models import Penalty, CompletionsResponse
from ai21.types import NotGiven, NOT_GIVEN
from ai21.utils.typing import remove_not_given


class BedrockCompletion(BedrockResource):
    def create(
        self,
        prompt: str,
        *,
        max_tokens: int | NotGiven = NOT_GIVEN,
        num_results: int | NotGiven = NOT_GIVEN,
        min_tokens: int | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        top_k_return: int | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        frequency_penalty: Penalty | NotGiven = NOT_GIVEN,
        presence_penalty: Penalty | NotGiven = NOT_GIVEN,
        count_penalty: Penalty | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> CompletionsResponse:
        body = remove_not_given(
            {
                "prompt": prompt,
                "maxTokens": max_tokens,
                "numResults": num_results,
                "minTokens": min_tokens,
                "temperature": temperature,
                "topP": top_p,
                "topKReturn": top_k_return,
                "stopSequences": stop_sequences or [],
                "frequencyPenalty": frequency_penalty.to_dict() if frequency_penalty else frequency_penalty,
                "presencePenalty": presence_penalty.to_dict() if presence_penalty else presence_penalty,
                "countPenalty": count_penalty.to_dict() if count_penalty else count_penalty,
            }
        )

        model_id = kwargs.get("model_id", self._model_id)

        if model_id is None:
            raise ValueError("model_id should be provided in either the constructor or the 'create' method call")

        raw_response = self._invoke(model_id=model_id, body=body)

        return CompletionsResponse.from_dict(raw_response)
