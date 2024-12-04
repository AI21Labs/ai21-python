from datetime import datetime
from typing import List

from ai21.models.ai21_base_model import AI21BaseModel


class RouteResponse(AI21BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    assistant_id: str
    plan_id: str
    name: str
    description: str
    examples: List[str]


class ListRouteResponse(AI21BaseModel):
    results: List[RouteResponse]
