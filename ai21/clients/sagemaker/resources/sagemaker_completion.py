from __future__ import annotations

from typing import List, Dict, cast

from ai21.clients.sagemaker.resources.sagemaker_resource import SageMakerResource, AsyncSageMakerResource
from ai21.models import Penalty, CompletionsResponse
from ai21.models._pydantic_compatibility import _from_dict
from ai21.types import NotGiven, NOT_GIVEN
from ai21.utils.typing import remove_not_given


class SageMakerCompletion(SageMakerResource):
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
        logit_bias: Dict[str, float] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> CompletionsResponse:
        """
        :param prompt: Text for model to complete
        :param max_tokens: The maximum number of tokens to generate per result
        :param num_results: Number of completions to sample and return.
        :param min_tokens: The minimum number of tokens to generate per result.
        :param temperature: A value controlling the "creativity" of the model's responses.
        :param top_p: A value controlling the diversity of the model's responses.
        :param top_k_return: The number of top-scoring tokens to consider for each generation step.
        :param stop_sequences: Stops decoding if any of the strings is generated
        :param frequency_penalty: A penalty applied to tokens that are frequently generated.
        :param presence_penalty:  A penalty applied to tokens that are already present in the prompt.
        :param count_penalty: A penalty applied to tokens based on their frequency in the generated responses
        :param logit_bias: A dictionary which contains mapping from strings to floats, where the strings are text
        representations of the tokens and the floats are the biases themselves. A positive bias increases generation
        probability for a given token and a negative bias decreases it.
        :param kwargs:
        :return:
        """
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
                "logitBias": logit_bias,
            }
        )

        raw_response = self._post(body=body)

        return cast(_from_dict(obj=CompletionsResponse, obj_dict=raw_response.json()), CompletionsResponse)


class AsyncSageMakerCompletion(AsyncSageMakerResource):
    async def create(
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
        logit_bias: Dict[str, float] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> CompletionsResponse:
        """
        :param prompt: Text for model to complete
        :param max_tokens: The maximum number of tokens to generate per result
        :param num_results: Number of completions to sample and return.
        :param min_tokens: The minimum number of tokens to generate per result.
        :param temperature: A value controlling the "creativity" of the model's responses.
        :param top_p: A value controlling the diversity of the model's responses.
        :param top_k_return: The number of top-scoring tokens to consider for each generation step.
        :param stop_sequences: Stops decoding if any of the strings is generated
        :param frequency_penalty: A penalty applied to tokens that are frequently generated.
        :param presence_penalty:  A penalty applied to tokens that are already present in the prompt.
        :param count_penalty: A penalty applied to tokens based on their frequency in the generated responses
        :param logit_bias: A dictionary which contains mapping from strings to floats, where the strings are text
        representations of the tokens and the floats are the biases themselves. A positive bias increases generation
        probability for a given token and a negative bias decreases it.
        :param kwargs:
        :return:
        """
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
                "logitBias": logit_bias,
            }
        )

        raw_response = await self._post(body=body)

        return cast(_from_dict(obj=CompletionsResponse, obj_dict=raw_response.json()), CompletionsResponse)
