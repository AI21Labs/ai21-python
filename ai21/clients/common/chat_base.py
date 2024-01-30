from abc import ABC, abstractmethod
from typing import List, Any, Dict, Optional

from ai21.models.chat_message import ChatMessage
from ai21.models.penalty import Penalty
from ai21.models.responses.chat_response import ChatResponse


class Chat(ABC):
    _module_name = "chat"

    @abstractmethod
    def create(
        self,
        model: str,
        messages: List[ChatMessage],
        system: str,
        *,
        num_results: Optional[int] = 1,
        temperature: Optional[float] = 0.7,
        max_tokens: Optional[int] = 300,
        min_tokens: Optional[int] = 0,
        top_p: Optional[float] = 1.0,
        top_k_return: Optional[int] = 0,
        stop_sequences: Optional[List[str]] = None,
        frequency_penalty: Optional[Penalty] = None,
        presence_penalty: Optional[Penalty] = None,
        count_penalty: Optional[Penalty] = None,
        **kwargs,
    ) -> ChatResponse:
        """

        :param model: model type you wish to interact with
        :param messages: A sequence of messages ingested by the model, which then returns the assistant's response
        :param system: Offers the model overarching guidance on its response approach, encapsulating context, tone,
         guardrails, and more
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
        :param kwargs:
        :return:
        """
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> ChatResponse:
        return ChatResponse.from_dict(json)

    def _create_body(
        self,
        model: str,
        messages: List[ChatMessage],
        system: str,
        num_results: Optional[int] = 1,
        temperature: Optional[float] = 0.7,
        max_tokens: Optional[int] = 300,
        min_tokens: Optional[int] = 0,
        top_p: Optional[float] = 1.0,
        top_k_return: Optional[int] = 0,
        stop_sequences: Optional[List[str]] = None,
        frequency_penalty: Optional[Penalty] = None,
        presence_penalty: Optional[Penalty] = None,
        count_penalty: Optional[Penalty] = None,
    ) -> Dict[str, Any]:
        return {
            "model": model,
            "system": system,
            "messages": [message.to_dict() for message in messages],
            "temperature": temperature,
            "maxTokens": max_tokens,
            "minTokens": min_tokens,
            "numResults": num_results,
            "topP": top_p,
            "topKReturn": top_k_return,
            "stopSequences": stop_sequences,
            "frequencyPenalty": None if frequency_penalty is None else frequency_penalty.to_dict(),
            "presencePenalty": None if presence_penalty is None else presence_penalty.to_dict(),
            "countPenalty": None if count_penalty is None else count_penalty.to_dict(),
        }
