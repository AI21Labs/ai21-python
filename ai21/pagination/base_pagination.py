from __future__ import annotations

from typing import Any, Callable, Dict, Generic, List, Protocol, Sequence, TypeVar

from ai21.models._pydantic_compatibility import _from_dict


class HasId(Protocol):
    id: str


PageT = TypeVar("PageT", bound=HasId)


def cast_page_response(raw_response: Dict[str, Any], response_cls: PageT) -> List[PageT]:
    """Cast API response to appropriate types."""
    return [_from_dict(obj=response_cls, obj_dict=item) for item in raw_response]


class BasePagination(Generic[PageT]):
    def __init__(
        self,
        request_callback: Callable,
        path: str,
        response_cls: PageT,
        params: Dict[str, Any] | None = None,
        **kwargs: Any,
    ):
        self.request_callback = request_callback
        self.path = path
        self.params = params or {}
        self.response_cls = response_cls
        self.kwargs = kwargs

    def _set_next_page_params(self, response: Sequence[PageT]) -> None:
        """Update params with the ID from the last item in the response."""
        if response:
            self.params["after"] = response[-1].id
