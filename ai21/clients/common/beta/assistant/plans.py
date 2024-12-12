from __future__ import annotations

import inspect
from abc import ABC, abstractmethod
from typing import Any, Dict, Type

from pydantic import BaseModel

from ai21.models.responses.plan_response import PlanResponse, ListPlanResponse
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class BasePlans(ABC):
    _module_name = "plans"

    @abstractmethod
    def create(
        self,
        *,
        assistant_id: str,
        code: str | callable,
        schemas: list[dict] | list[Type[BaseModel]] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> PlanResponse:
        pass

    def _create_body(
        self,
        *,
        code: str | callable,
        schemas: list[dict] | list[Type[BaseModel]] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> Dict[str, Any]:
        if callable(code):
            code = inspect.getsource(code).strip()

        schema_dicts = []
        for schema in schemas:
            if inspect.isclass(schema) and issubclass(schema, BaseModel):
                schema_dicts.append(schema.model_json_schema())
            else:
                schema_dicts.append(schema)

        return remove_not_given(
            {
                "code": code,
                "schemas": schema_dicts,
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
        schemas: list[dict] | NotGiven = NOT_GIVEN,
    ) -> PlanResponse:
        pass
