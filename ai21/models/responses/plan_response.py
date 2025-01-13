from datetime import datetime
from typing import List, Optional, Dict, Any

from ai21.models.ai21_base_model import AI21BaseModel


class PlanResponse(AI21BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    assistant_id: str
    code: str
    schemas: Optional[List[Dict[str, Any]]] = None


class ListPlanResponse(AI21BaseModel):
    results: List[PlanResponse]


class PlanValidationResponse(AI21BaseModel):
    is_valid: bool
    message: Optional[str] = None
    details: Optional[str] = None
