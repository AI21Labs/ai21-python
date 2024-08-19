from typing import Optional, Dict

from ai21.models.ai21_base_model import AI21BaseModel


class DocumentSchema(AI21BaseModel):
    content: str
    id: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
