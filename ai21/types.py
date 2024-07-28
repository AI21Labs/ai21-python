from typing import Any, Union, List

import httpx
from typing_extensions import Literal, TypeVar, TYPE_CHECKING

from ai21.stream.async_stream import AsyncStream
from ai21.stream.stream import Stream

if TYPE_CHECKING:
    from ai21.models.ai21_base_model import AI21BaseModel  # noqa

ResponseT = TypeVar("_ResponseT", bound=Union["AI21BaseModel", str, httpx.Response, List[Any]])
StreamT = TypeVar("_StreamT", bound=Stream[Any])
AsyncStreamT = TypeVar("_AsyncStreamT", bound=AsyncStream[Any])


# Sentinel class used until PEP 0661 is accepted
class NotGiven:
    """
    A sentinel singleton class used to distinguish omitted keyword arguments
    from those passed in with the value None (which may have different behavior).

    For example:

    ```py
    def get(timeout: Union[int, NotGiven, None] = NotGiven()) -> Response:
        ...


    get(timeout=1)  # 1s timeout
    get(timeout=None)  # No timeout
    get()  # Default timeout behavior, which may not be statically known at the method definition.
    ```
    """

    def __bool__(self) -> Literal[False]:
        return False

    def __repr__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN = NotGiven()
