from ai21.models.ai21_base_model import AI21BaseModel
from ai21.models.chat.role_type import RoleType


class ChatMessage(AI21BaseModel):
    role: RoleType
    text: str
