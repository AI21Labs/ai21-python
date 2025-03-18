from __future__ import annotations

from typing import Any, Callable, Dict, Iterator, List, Type

from .base_pagination import BasePagination, PageT, cast_page_response


class SyncPagination(BasePagination[PageT]):
    """A wrapper class that provides synchronous pagination functionality for API resources."""

    def __init__(
        self,
        request_callback: Callable,
        path: str,
        params: Dict[str, Any] | None = None,
        response_cls: Type[PageT] | None = None,
        **kwargs: Any,
    ):
        super().__init__(request_callback, path, params, response_cls, **kwargs)
        self._iterator = self.__paginate__()

    def __iter__(self) -> Iterator[List[PageT]]:
        for page in self._iterator:
            yield page

    def __next__(self) -> List[Any]:
        return self._iterator.__next__()

    def __paginate__(self) -> Iterator[List[PageT]]:
        while True:
            results = self.request_method(path=self.path, params=self.params, method="GET", **self.kwargs)
            response = cast_page_response(results, self.response_cls)

            if not response:
                break

            self._next_page_params(response)
            yield response
