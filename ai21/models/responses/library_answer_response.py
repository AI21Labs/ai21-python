from typing import List, Optional

from ai21.models.ai21_base_model import AI21BaseModel


class SourceDocument(AI21BaseModel):
    file_id: str
    name: str
    highlights: List[str]
    public_url: Optional[str] = None


class LibraryAnswerResponse(AI21BaseModel):
    id: str
    answer_in_context: bool
    answer: Optional[str] = None
    sources: Optional[List[SourceDocument]] = None
