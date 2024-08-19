from typing import Optional
from ai21.models.ai21_base_model import AI21BaseModel


class DocumentSchema(AI21BaseModel):
    id: Optional[str] = None
    content: str
    metadata: Optional[dict[str, str]] = None
