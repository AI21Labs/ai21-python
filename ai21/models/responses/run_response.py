from datetime import datetime
from typing import Optional

from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.assistant.assistant import Optimization
from ai21.models.assistant.run import RunStatus, RequiredAction


class RunResponse(AI21BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    thread_id: str
    assistant_id: str
    description: Optional[str] = None
    status: RunStatus
    optimization: Optimization
    execution_id: Optional[str] = None
    required_action: Optional[RequiredAction] = None
    error: Optional[str] = None
