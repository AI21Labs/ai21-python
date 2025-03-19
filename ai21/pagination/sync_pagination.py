from __future__ import annotations

from typing import Any, Callable, Dict, Iterator, List

from .base_pagination import BasePagination, PageT, cast_page_response


class SyncPagination(BasePagination[PageT]):
    """A wrapper class that provides synchronous pagination functionality for API resources."""

    def __init__(
        self,
        request_callback: Callable,
        path: str,
        response_cls: PageT,
        params: Dict[str, Any] | None = None,
        **kwargs: Any,
    ):
        super().__init__(request_callback, path, response_cls, params, **kwargs)
        self._iterator = self.__paginate__()

    def __iter__(self) -> Iterator[List[PageT]]:
        for page in self._iterator:
            yield page

    def __next__(self) -> List[Any]:
        return self._iterator.__next__()

    def __paginate__(self) -> Iterator[List[PageT]]:
        while True:
            results = self.request_callback(path=self.path, params=self.params, method="GET", **self.kwargs)
            response = cast_page_response(raw_response=results.json(), response_cls=self.response_cls)

            if not response:
                break

            self._set_next_page_params(response)
            yield response
