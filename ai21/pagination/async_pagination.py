from __future__ import annotations

from typing import Any, AsyncIterator, Callable, Dict, List

from .base_pagination import BasePagination, PageT, cast_page_response


class AsyncPagination(BasePagination[PageT]):
    """A wrapper class that provides asynchronous pagination functionality for API resources."""

    def __init__(
        self,
        request_callback: Callable,
        path: str,
        response_cls: PageT,
        params: Dict[str, Any] | None = None,
    ):
        super().__init__(request_callback, path, response_cls, params)
        self._iterator = self.__paginate__()

    async def __aiter__(self) -> AsyncIterator[List[PageT]]:
        async for page in self._iterator:
            yield page

    async def __anext__(self) -> List[PageT]:
        return await self._iterator.__anext__()

    async def __paginate__(self) -> AsyncIterator[List[PageT]]:
        while True:
            results = await self.request_callback(path=self.path, params=self.params, method="GET")
            response = cast_page_response(raw_response=results.json(), response_cls=self.response_cls)

            if not response:
                break

            self._set_next_page_params(response)
            yield response
