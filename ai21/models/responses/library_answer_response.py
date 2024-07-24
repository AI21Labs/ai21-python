from typing import List, Optional

from pydantic import Field

from ai21.models.ai21_base_model import AI21BaseModel


class SourceDocument(AI21BaseModel):
    file_id: str = Field(alias="fileId")
    name: str
    highlights: List[str]
    public_url: Optional[str] = Field(default=None, alias="publicUrl")


class LibraryAnswerResponse(AI21BaseModel):
    id: str
    answer_in_context: bool = Field(alias="answerInContext")
    answer: Optional[str] = None
    sources: Optional[List[SourceDocument]] = None
