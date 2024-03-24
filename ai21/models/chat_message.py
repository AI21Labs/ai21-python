import warnings
from dataclasses import dataclass
from typing import Optional

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin
from ai21.models.role_type import RoleType


@dataclass
class ChatMessage(AI21BaseModelMixin):
    role: RoleType
    text: Optional[str] = None
    content: Optional[str] = None

    def __call__(self, *args, **kwargs):
        if self.text is None and self.content is not None:
            raise ValueError("'content' field or 'text' field must be provided")

        if self.text is not None and self.content is None:
            warnings.warn("'text' field is deprecated, please use 'content' field instead", DeprecationWarning)
            self.content = self.text
