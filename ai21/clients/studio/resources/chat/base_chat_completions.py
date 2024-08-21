from __future__ import annotations

import warnings
from abc import ABC
from typing import List, Optional, Union, Any, Dict, Literal

from ai21.models.chat.chat_message import ChatMessageParam
from ai21.models.chat.document_schema import DocumentSchema
from ai21.models.chat.response_format import ResponseFormat
from ai21.models.chat.tool_defintions import ToolDefinition
from ai21.types import NotGiven
from ai21.utils.typing import remove_not_given
from ai21.models._pydantic_compatibility import _to_dict


class BaseChatCompletions(ABC):
    _module_name = "chat/completions"

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

    def _create_body(
        self,
        model: str,
        messages: List[ChatMessageParam],
        max_tokens: Optional[int] | NotGiven,
        temperature: Optional[float] | NotGiven,
        top_p: Optional[float] | NotGiven,
        stop: Optional[Union[str, List[str]]] | NotGiven,
        n: Optional[int] | NotGiven,
        stream: Literal[False] | Literal[True] | NotGiven,
        tools: List[ToolDefinition] | NotGiven,
        response_format: ResponseFormat | NotGiven,
        documents: List[DocumentSchema] | NotGiven,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        return remove_not_given(
            {
                "model": model,
                "messages": [_to_dict(message) for message in messages],
                "temperature": temperature,
                "max_tokens": max_tokens,
                "top_p": top_p,
                "stop": stop,
                "n": n,
                "stream": stream,
                "tools": tools,
                "response_format": response_format,
                "documents": documents,
                **kwargs,
            }
        )
