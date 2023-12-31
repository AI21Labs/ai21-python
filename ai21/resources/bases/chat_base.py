from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Any, Dict, Optional

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin
from ai21.resources.models.penalty import Penalty
from ai21.resources.models.role_type import RoleType
from ai21.resources.responses.chat_response import ChatResponse


@dataclass
class Message(AI21BaseModelMixin):
    role: RoleType
    text: str
    name: Optional[str]


class Chat(ABC):
    _module_name = "chat"

    @abstractmethod
    def create(
        self,
        model: str,
        messages: List[Message],
        system: str,
        *,
        num_results: Optional[int] = 1,
        temperature: Optional[float] = 0.7,
        max_tokens: Optional[int] = 300,
        min_tokens: Optional[int] = 0,
        top_p: Optional[float] = 1.0,
        top_k_returns: Optional[int] = 0,
        stop_sequences: Optional[List[str]] = None,
        frequency_penalty: Optional[Penalty] = None,
        presence_penalty: Optional[Penalty] = None,
        count_penalty: Optional[Penalty] = None,
        **kwargs,
    ) -> ChatResponse:
        pass

    def _json_to_response(self, json: Dict[str, Any]) -> ChatResponse:
        return ChatResponse.from_dict(json)

    def _create_body(
        self,
        model: str,
        messages: List[Message],
        system: str,
        num_results: Optional[int] = 1,
        temperature: Optional[float] = 0.7,
        max_tokens: Optional[int] = 300,
        min_tokens: Optional[int] = 0,
        top_p: Optional[float] = 1.0,
        top_k_returns: Optional[int] = 0,
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
            "topKReturn": top_k_returns,
            "stopSequences": stop_sequences,
            "frequencyPenalty": None if frequency_penalty is None else frequency_penalty.to_dict(),
            "presencePenalty": None if presence_penalty is None else presence_penalty.to_dict(),
            "countPenalty": None if count_penalty is None else count_penalty.to_dict(),
        }
