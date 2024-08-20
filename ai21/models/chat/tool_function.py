from ai21.models.ai21_base_model import AI21BaseModel


class ToolFunction(AI21BaseModel):
    name: str
    arguments: str
