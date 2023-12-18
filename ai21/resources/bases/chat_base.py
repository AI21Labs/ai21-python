from abc import ABC, abstractmethod
from typing import List, Any, Dict, Optional

from ai21.resources.responses.chat_response import ChatResponse


class Message:
    role: str
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
        frequency_penalty: Optional[Dict[str, Any]] = None,
        presence_penalty: Optional[Dict[str, Any]] = None,
        count_penalty: Optional[Dict[str, Any]] = None,
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
        frequency_penalty: Optional[Dict[str, Any]] = None,
        presence_penalty: Optional[Dict[str, Any]] = None,
        count_penalty: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return {
            "model": model,
            "system": system,
            "messages": messages,
            "temperature": temperature,
            "maxTokens": max_tokens,
            "minTokens": min_tokens,
            "numResults": num_results,
            "topP": top_p,
            "topKReturn": top_k_returns,
            "stopSequences": stop_sequences,
            "frequencyPenalty": frequency_penalty,
            "presencePenalty": presence_penalty,
            "countPenalty": count_penalty,
        }
