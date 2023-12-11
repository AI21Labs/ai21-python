from ai21.models.ai21_base_model import AI21BaseModel


class SummarizeResponse(AI21BaseModel):
    id: str
    summary: str
