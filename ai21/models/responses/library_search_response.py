from typing import Optional, List

from ai21.models.ai21_base_model import AI21BaseModel


class LibrarySearchResult(AI21BaseModel):
    text: str
    file_id: str
    file_name: str
    score: float
    order: Optional[int] = None
    public_url: Optional[str] = None
    labels: Optional[List[str]] = None


class LibrarySearchResponse(AI21BaseModel):
    id: str
    results: List[LibrarySearchResult]
