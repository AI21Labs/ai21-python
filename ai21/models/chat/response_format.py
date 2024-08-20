from typing import Literal

from ai21.models.ai21_base_model import AI21BaseModel


class ResponseFormat(AI21BaseModel):
    type: Literal["text", "json_object"]
