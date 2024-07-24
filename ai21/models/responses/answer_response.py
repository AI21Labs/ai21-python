from typing import Optional

from pydantic import Field

from ai21.models.ai21_base_model import AI21BaseModel


class AnswerResponse(AI21BaseModel):
    id: str
    answer_in_context: Optional[bool] = Field(default=None, alias="answerInContext")
    answer: Optional[str] = None
