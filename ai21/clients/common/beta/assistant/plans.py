from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict

from ai21.models.responses.plan_response import PlanResponse, ListPlanResponse
from ai21.utils.typing import remove_not_given


class BasePlans(ABC):
    _module_name = "plans"

    @abstractmethod
    def create(
        self,
        *,
        assistant_id: str,
        code: str,
        **kwargs,
    ) -> PlanResponse:
        pass

    def _create_body(
        self,
        *,
        code: str,
        **kwargs,
    ) -> Dict[str, Any]:
        return remove_not_given(
            {
                "code": code,
                **kwargs,
            }
        )

    @abstractmethod
    def list(
        self,
        *,
        assistant_id: str,
    ) -> ListPlanResponse:
        pass

    @abstractmethod
    def retrieve(
        self,
        *,
        assistant_id: str,
        plan_id: str,
    ) -> PlanResponse:
        pass

    @abstractmethod
    def modify(
        self,
        *,
        assistant_id: str,
        plan_id: str,
        code: str,
    ) -> PlanResponse:
        pass
