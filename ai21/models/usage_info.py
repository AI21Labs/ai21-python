from dataclasses import dataclass

from ai21.models.ai21_base_model_mixin import AI21BaseModelMixin


@dataclass
class UsageInfo(AI21BaseModelMixin):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
