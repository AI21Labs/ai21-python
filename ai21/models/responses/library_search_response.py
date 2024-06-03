from dataclasses import dataclass
from typing import Optional, List

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class LibrarySearchResult(AI21BaseModelMixin):
    text: str
    file_id: str
    file_name: str
    score: float
    order: Optional[int] = None
    public_url: Optional[str] = None
    labels: Optional[List[str]] = None


@dataclass
class LibrarySearchResponse(AI21BaseModelMixin):
    id: str
    results: List[LibrarySearchResult]
