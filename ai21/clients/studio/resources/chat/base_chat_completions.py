from __future__ import annotations

from abc import ABC
from typing import List, Optional, Union, Any, Dict, Literal

from ai21.models.chat import ChatMessage
from ai21.types import NotGiven
from ai21.utils.typing import remove_not_given


class BaseChatCompletions(ABC):
    _module_name = "chat/completions"

    def _create_body(
        self,
        model: str,
        messages: List[ChatMessage],
        max_tokens: Optional[int] | NotGiven,
        temperature: Optional[float] | NotGiven,
        top_p: Optional[float] | NotGiven,
        stop: Optional[Union[str, List[str]]] | NotGiven,
        n: Optional[int] | NotGiven,
        stream: Literal[False] | Literal[True] | NotGiven,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        return remove_not_given(
            {
                "model": model,
                "messages": [message.to_dict() for message in messages],
                "temperature": temperature,
                "max_tokens": max_tokens,
                "top_p": top_p,
                "stop": stop,
                "n": n,
                "stream": stream,
                **kwargs,
            }
        )
