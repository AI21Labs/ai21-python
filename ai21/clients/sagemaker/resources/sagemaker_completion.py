from typing import Optional, List, Dict

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
        logit_bias: Optional[Dict[str, float]] = None,
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

        if logit_bias is not None:
            body["logitBias"] = logit_bias

        raw_response = self._invoke(body)

        return CompletionsResponse.from_dict(raw_response)
