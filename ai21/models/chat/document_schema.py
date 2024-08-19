from __future__ import annotations
from typing import Optional
from pydantic import Field
from ai21.models.ai21_base_model import AI21BaseModel


class DocumentSchema(AI21BaseModel):
    id: Optional[str] = Field(None, description="Id of the document")
    content: str = Field(description="Content of the document")
    metadata: Optional[dict[str, str]] = Field({}, description="Metadata of the document")
