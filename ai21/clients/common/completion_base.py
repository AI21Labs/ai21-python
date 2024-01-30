from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any

from ai21.models import Penalty
from ai21.models.responses.completion_response import CompletionsResponse


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
        frequency_penalty: Optional[Penalty] = None,
        presence_penalty: Optional[Penalty] = None,
        count_penalty: Optional[Penalty] = None,
        epoch: Optional[int] = None,
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
        :param kwargs:
        :return:
        """
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
        frequency_penalty: Optional[Penalty],
        presence_penalty: Optional[Penalty],
        count_penalty: Optional[Penalty],
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
            "frequencyPenalty": None if frequency_penalty is None else frequency_penalty.to_dict(),
            "presencePenalty": None if presence_penalty is None else presence_penalty.to_dict(),
            "countPenalty": None if count_penalty is None else count_penalty.to_dict(),
            "epoch": epoch,
        }
