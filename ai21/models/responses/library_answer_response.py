from dataclasses import dataclass
from typing import List, Optional

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class SourceDocument(AI21BaseModelMixin):
    file_id: str
    name: str
    highlights: List[str]
    public_url: Optional[str] = None


@dataclass
class LibraryAnswerResponse(AI21BaseModelMixin):
    id: str
    answer_in_context: bool
    answer: Optional[str] = None
    sources: Optional[List[SourceDocument]] = None
