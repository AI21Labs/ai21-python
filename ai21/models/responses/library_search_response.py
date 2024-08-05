from typing import Optional, List

from pydantic import Field

from ai21.models.ai21_base_model import AI21BaseModel


class LibrarySearchResult(AI21BaseModel):
    text: str
    file_id: str = Field(alias="fileId")
    file_name: str = Field(alias="fileName")
    score: float
    order: Optional[int] = None
    public_url: Optional[str] = Field(default=None, alias="publicUrl")
    labels: Optional[List[str]] = None


class LibrarySearchResponse(AI21BaseModel):
    id: str
    results: List[LibrarySearchResult]
