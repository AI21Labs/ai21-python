from typing import List

from ai21.models.ai21_base_model import AI21BaseModel


class EmbedResult(AI21BaseModel):
    embedding: List[float]

    def __init__(self, embedding: List[float]):
        super().__init__(embedding=embedding)


class EmbedResponse(AI21BaseModel):
    id: str
    results: List[EmbedResult]
