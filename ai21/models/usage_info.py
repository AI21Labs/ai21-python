from ai21.models.ai21_base_model import AI21BaseModel


class UsageInfo(AI21BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
