from __future__ import annotations

import warnings
from abc import ABC, abstractmethod
from typing import List, Dict, Optional

from ai21.models import Penalty, CompletionsResponse
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given
from ai21.models._pydantic_compatibility import _to_dict


class Completion(ABC):
    _module_name = "complete"

    def _get_model(self, model: Optional[str], model_id: Optional[str]) -> str:
        if model_id is not None:
            warnings.warn(
                "The 'model_id' parameter is deprecated and will be removed in a future version."
                " Please use 'model' instead.",
                DeprecationWarning,
                stacklevel=2,
            )

        if model_id and model:
            raise ValueError("Please provide only 'model' as 'model_id' is deprecated.")

        if not model and not model_id:
            raise ValueError("model should be provided 'create' method call")

        return model or model_id

    @abstractmethod
    def create(
        self,
        model: str,
        prompt: str,
        *,
        max_tokens: int | NotGiven = NOT_GIVEN,
        num_results: int | NotGiven = NOT_GIVEN,
        min_tokens: int | NotGiven = NOT_GIVEN,
        temperature: float | NOT_GIVEN = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        top_k_return: int | NotGiven = NOT_GIVEN,
        custom_model: str | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        frequency_penalty: Penalty | NotGiven = NOT_GIVEN,
        presence_penalty: Penalty | NotGiven = NOT_GIVEN,
        count_penalty: Penalty | NotGiven = NOT_GIVEN,
        epoch: int | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, float] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> CompletionsResponse:
        """
        :param model: model type you wish to interact with
        :param prompt: Text for model to complete
        :param max_tokens: The maximum number of tokens to generate per result
        :param num_results: Number of completions to sample and return.
        :param min_tokens: The minimum number of tokens to generate per result.
        :param temperature: A value controlling the "creativity" of the model's responses.
        :param top_p: A value controlling the diversity of the model's responses.
        :param top_k_return: The number of top-scoring tokens to consider for each generation step.
        :param custom_model:
        :param stop_sequences: Stops decoding if any of the strings is generated
        :param frequency_penalty: A penalty applied to tokens that are frequently generated.
        :param presence_penalty:  A penalty applied to tokens that are already present in the prompt.
        :param count_penalty: A penalty applied to tokens based on their frequency in the generated responses
        :param epoch:
        :param logit_bias: A dictionary which contains mapping from strings to floats, where the strings are text
        representations of the tokens and the floats are the biases themselves. A positive bias increases generation
        probability for a given token and a negative bias decreases it.
        :param kwargs:
        :return:
        """
        pass

    def _create_body(
        self,
        model: str,
        prompt: str,
        max_tokens: int | NotGiven,
        num_results: int | NotGiven,
        min_tokens: int | NotGiven,
        temperature: float | NotGiven,
        top_p: float | NotGiven,
        top_k_return: int | NotGiven,
        custom_model: str | NotGiven,
        stop_sequences: List[str] | NotGiven,
        frequency_penalty: Penalty | NotGiven,
        presence_penalty: Penalty | NotGiven,
        count_penalty: Penalty | NotGiven,
        epoch: int | NotGiven,
        logit_bias: Dict[str, float] | NotGiven,
        **kwargs,
    ):
        return remove_not_given(
            {
                "model": model,
                "customModel": custom_model,
                "prompt": prompt,
                "maxTokens": max_tokens,
                "numResults": num_results,
                "minTokens": min_tokens,
                "temperature": temperature,
                "topP": top_p,
                "topKReturn": top_k_return,
                "stopSequences": stop_sequences,
                "frequencyPenalty": (NOT_GIVEN if frequency_penalty is NOT_GIVEN else _to_dict(frequency_penalty)),
                "presencePenalty": (NOT_GIVEN if presence_penalty is NOT_GIVEN else _to_dict(presence_penalty)),
                "countPenalty": (NOT_GIVEN if count_penalty is NOT_GIVEN else _to_dict(count_penalty)),
                "epoch": epoch,
                "logitBias": logit_bias,
                **kwargs,
            }
        )

    def _get_completion_path(self, model: str, custom_model: str | NotGiven = NOT_GIVEN):
        path = f"/{model}"

        if custom_model:
            path = f"{path}/{custom_model}"

        path = f"{path}/{self._module_name}"

        return path
