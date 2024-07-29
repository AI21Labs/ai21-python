from typing import List

from ai21.models.ai21_base_model import AI21BaseModel


class Suggestion(AI21BaseModel):
    text: str


class ParaphraseResponse(AI21BaseModel):
    id: str
    suggestions: List[Suggestion]
