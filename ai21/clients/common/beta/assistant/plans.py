from __future__ import annotations

import inspect
from abc import ABC, abstractmethod
from typing import Any, Dict, Type, Callable, List

from pydantic import BaseModel

from ai21.errors import CodeParsingError
from ai21.models._pydantic_compatibility import _to_schema
from ai21.models.responses.plan_response import PlanResponse, ListPlanResponse
from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class BasePlans(ABC):
    _module_name = "plans"

    def _parse_schema(self, schema: Type[BaseModel] | Dict[str, Any]) -> Dict[str, Any]:
        if inspect.isclass(schema) and issubclass(schema, BaseModel):
            return _to_schema(schema)
        return schema

    def _parse_code(self, code: str | Callable) -> str:
        if callable(code):
            try:
                return inspect.getsource(code).strip()
            except OSError as e:
                raise CodeParsingError(str(e))
            except Exception:
                raise CodeParsingError()
        return code

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
        schemas: List[Dict[str, Any]] | List[BaseModel] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> Dict[str, Any]:
        code_str = self._parse_code(code)

        return remove_not_given(
            {
                "code": code_str,
                "schemas": (
                    [self._parse_schema(schema) for schema in schemas] if schemas is not NOT_GIVEN else NOT_GIVEN
                ),
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
