from __future__ import annotations

import inspect
from abc import ABC, abstractmethod
from typing import Any, Dict, Type, Callable, List

from pydantic import BaseModel

from ai21.models.responses.plan_response import PlanResponse, ListPlanResponse
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


def _parse_schema(schema: Type[BaseModel] | Dict[str, Any]) -> Dict[str, Any]:
    if inspect.isclass(schema) and issubclass(schema, BaseModel):
        return schema.model_json_schema()
    return schema


def _parse_code(code: str | Callable) -> str:
    if callable(code):
        return inspect.getsource(code).strip()


class BasePlans(ABC):
    _module_name = "plans"

    @abstractmethod
    def create(
        self,
        *,
        assistant_id: str,
        code: str | Callable,
        schemas: List[Dict[str, Any]] | List[Type[BaseModel]] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> PlanResponse:
        pass

    def _create_body(
        self,
        *,
        code: str | Callable,
        schemas: List[Dict[str, Any]] | List[Type[BaseModel]] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> Dict[str, Any]:
        code_str = _parse_code(code)

        schema_dicts = [_parse_schema(schema) for schema in schemas]

        return remove_not_given(
            {
                "code": code_str,
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
        schemas: List[Dict[str, Any]] | NotGiven = NOT_GIVEN,
    ) -> PlanResponse:
        pass
