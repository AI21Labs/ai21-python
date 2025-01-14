from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from ai21.models.responses.route_response import RouteResponse, ListRouteResponse
from ai21.types import NotGiven, NOT_GIVEN
from ai21.utils.typing import remove_not_given


class BaseRoutes(ABC):
    _module_name = "routes"

    @abstractmethod
    def create(
        self,
        *,
        assistant_id: str,
        plan_id: str,
        name: str,
        examples: List[str],
        description: str | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> RouteResponse:
        pass

    def _create_body(
        self,
        *,
        plan_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        examples: List[str] | NotGiven = NOT_GIVEN,
        **kwargs,
    ) -> Dict[str, Any]:
        return remove_not_given(
            {
                "plan_id": plan_id,
                "name": name,
                "description": description,
                "examples": examples,
                **kwargs,
            }
        )

    @abstractmethod
    def retrieve(
        self,
        *,
        assistant_id: str,
        route_id: str,
    ) -> RouteResponse:
        pass

    @abstractmethod
    def list(
        self,
        *,
        assistant_id: str,
        name: str | NotGiven = NotGiven,
    ) -> ListRouteResponse:
        pass

    @abstractmethod
    def modify(
        self,
        *,
        assistant_id: str,
        route_id: str,
        description: str | NotGiven = NOT_GIVEN,
        examples: List[str] | NotGiven = NOT_GIVEN,
    ) -> RouteResponse:
        pass

    @abstractmethod
    def delete(self, *, assistant_id: str, route_id: str):
        pass
