from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    List,
    Optional,
    Protocol,
    Sequence,
    Type,
    TypeVar,
)

from ai21.models._pydantic_compatibility import _from_dict


class HasId(Protocol):
    id: str


PageT = TypeVar("PageT", bound=HasId)


def cast_page_response(response, response_cls) -> List[Any]:
    """Cast API response to appropriate types."""
    return [_from_dict(obj=response_cls, obj_dict=item) for item in response.json()]


class BasePagination(Generic[PageT]):
    """Base class that provides common pagination functionality for API resources."""

    def __init__(
        self,
        request_callback: Callable,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        response_cls: Optional[Type[PageT]] = None,
        **kwargs: Any,
    ):
        self.request_method = request_callback
        self.path = path
        self.params = params or {}
        self.response_cls = response_cls
        self.kwargs = kwargs

    def _next_page_params(self, response: Sequence[PageT]) -> None:
        """Update params with the ID from the last item in the response."""
        if response:
            self.params["after"] = response[-1].id
