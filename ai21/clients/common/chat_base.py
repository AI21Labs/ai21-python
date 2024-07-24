from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Any, Dict, Optional, TypeVar, Union

from ai21.clients.studio.resources.chat import ChatCompletions, AsyncChatCompletions
from ai21.clients.studio.resources.constants import (
    CHAT_DEFAULT_NUM_RESULTS,
    CHAT_DEFAULT_TEMPERATURE,
    CHAT_DEFAULT_MAX_TOKENS,
    CHAT_DEFAULT_MIN_TOKENS,
    CHAT_DEFAULT_TOP_P,
    CHAT_DEFAULT_TOP_K_RETURN,
)
from ai21.models import Penalty, ChatResponse, ChatMessage
from ai21.models._pydantic_compatibility import _to_dict
from ai21.types import NotGiven, NOT_GIVEN
from ai21.utils.typing import remove_not_given

_ChatCompletionsT = TypeVar("_ChatCompletionsT", bound=Union[ChatCompletions, AsyncChatCompletions])


class Chat(ABC):
    _module_name = "chat"

    @abstractmethod
    def create(
        self,
        model: str,
        messages: List[ChatMessage],
        system: str,
        *,
        num_results: Optional[int] = CHAT_DEFAULT_NUM_RESULTS,
        temperature: Optional[float] = CHAT_DEFAULT_TEMPERATURE,
        max_tokens: Optional[int] = CHAT_DEFAULT_MAX_TOKENS,
        min_tokens: Optional[int] = CHAT_DEFAULT_MIN_TOKENS,
        top_p: Optional[float] = CHAT_DEFAULT_TOP_P,
        top_k_return: Optional[int] = CHAT_DEFAULT_TOP_K_RETURN,
        stop_sequences: Optional[List[str]] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[Penalty] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[Penalty] | NotGiven = NOT_GIVEN,
        count_penalty: Optional[Penalty] | NotGiven = NOT_GIVEN,
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

    @property
    @abstractmethod
    def completions(self) -> _ChatCompletionsT:
        pass

    def _create_body(
        self,
        model: str,
        messages: List[ChatMessage],
        system: str,
        num_results: Optional[int] = CHAT_DEFAULT_NUM_RESULTS,
        temperature: Optional[float] = CHAT_DEFAULT_TEMPERATURE,
        max_tokens: Optional[int] = CHAT_DEFAULT_MAX_TOKENS,
        min_tokens: Optional[int] = CHAT_DEFAULT_MIN_TOKENS,
        top_p: Optional[float] = CHAT_DEFAULT_TOP_P,
        top_k_return: Optional[int] = CHAT_DEFAULT_TOP_K_RETURN,
        stop_sequences: Optional[List[str]] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[Penalty] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[Penalty] | NotGiven = NOT_GIVEN,
        count_penalty: Optional[Penalty] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> Dict[str, Any]:
        return remove_not_given(
            {
                "model": model,
                "system": system,
                "messages": [_to_dict(message) for message in messages],
                "temperature": temperature,
                "maxTokens": max_tokens,
                "minTokens": min_tokens,
                "numResults": num_results,
                "topP": top_p,
                "topKReturn": top_k_return,
                "stopSequences": stop_sequences,
                "frequencyPenalty": (NOT_GIVEN if frequency_penalty is NOT_GIVEN else _to_dict(frequency_penalty)),
                "presencePenalty": (NOT_GIVEN if presence_penalty is NOT_GIVEN else _to_dict(presence_penalty)),
                "countPenalty": (NOT_GIVEN if count_penalty is NOT_GIVEN else _to_dict(count_penalty)),
                **kwargs,
            }
        )
