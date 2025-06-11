from __future__ import annotations

import warnings

from abc import ABC
from typing import Any, Dict, List, Literal, Optional, Union

from ai21.models._pydantic_compatibility import _to_dict
from ai21.models.chat.chat_message import ChatMessageParam
from ai21.models.chat.document_schema import DocumentSchema
from ai21.models.chat.response_format import ResponseFormat
from ai21.models.chat.tool_defintions import ToolDefinition
from ai21.types import NotGiven
from ai21.utils.typing import remove_not_given


_MODEL_DEPRECATION_WARNING = """
The 'jamba-1.5-mini' and 'jamba-1.5-large' models are deprecated and will
be removed in a future version.
Please use jamba-mini-1.6-2025-03 or jamba-large-1.6-2025-03 instead.
"""


class BaseChatCompletions(ABC):
    _module_name = "chat/completions"

    def _check_model(self, model: Optional[str]) -> str:
        if not model:
            raise ValueError("model should be provided 'create' method call")

        if model in ["jamba-1.5-mini", "jamba-1.5-large"]:
            warnings.warn(
                _MODEL_DEPRECATION_WARNING,
                DeprecationWarning,
                stacklevel=3,
            )

        return model

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
