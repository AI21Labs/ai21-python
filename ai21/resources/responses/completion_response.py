from dataclasses import dataclass
from typing import List, Optional, Union, Any, Dict

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class Prompt(AI21BaseModelMixin):
    text: Optional[str]
    tokens: Optional[List[Dict[str, Any]]] = None


@dataclass
class CompletionData(AI21BaseModelMixin):
    text: Optional[str]
    tokens: Optional[List[Dict[str, Any]]] = None


@dataclass
class CompletionFinishReason(AI21BaseModelMixin):
    reason: Optional[str] = None
    length: Optional[int] = None


@dataclass
class Completion(AI21BaseModelMixin):
    data: CompletionData
    finish_reason: CompletionFinishReason


@dataclass
class CompletionsResponse(AI21BaseModelMixin):
    id: Union[int, str]
    prompt: Prompt
    completions: List[Completion]
