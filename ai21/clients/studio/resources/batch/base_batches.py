from __future__ import annotations

from abc import ABC
from typing import Any, Dict

from ai21.types import NOT_GIVEN, NotGiven
from ai21.utils.typing import remove_not_given


class BaseBatches(ABC):
    _module_name = "batches"

    def _create_body(
        self,
        endpoint: str,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        return remove_not_given(
            {
                "endpoint": endpoint,
                "metadata": metadata,
                **kwargs,
            }
        )

    def _create_list_params(
        self,
        after: str | NotGiven,
        limit: int | NotGiven,
    ) -> Dict[str, Any]:
        return remove_not_given({"after": after, "limit": limit})
