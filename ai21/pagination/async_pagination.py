from __future__ import annotations

from typing import Any, AsyncIterator, Callable, Dict, List, Type

from .base_pagination import BasePagination, PageT, cast_page_response


class AsyncPagination(BasePagination[PageT]):
    """A wrapper class that provides asynchronous pagination functionality for API resources."""

    def __init__(
        self,
        request_callback: Callable,
        path: str,
        params: Dict[str, Any] | None = None,
        response_cls: Type[PageT] | None = None,
    ):
        super().__init__(request_callback, path, params, response_cls)
        self._iterator = self.__paginate__()

    async def __aiter__(self) -> AsyncIterator[List[PageT]]:
        async for page in self._iterator:
            yield page

    async def __anext__(self) -> List[PageT]:
        return await self._iterator.__anext__()

    async def __paginate__(self) -> AsyncIterator[List[PageT]]:
        while True:
            results = await self.request_method(path=self.path, params=self.params, method="GET")
            response = cast_page_response(results, self.response_cls)

            if not response:
                break

            self._next_page_params(response)
            yield response
