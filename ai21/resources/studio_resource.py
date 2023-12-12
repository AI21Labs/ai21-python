from __future__ import annotations

from abc import ABC
from typing import Any, Dict, Optional

from ai21.ai21_studio_client import AI21StudioClient


class StudioResource(ABC):
    def __init__(self, client: AI21StudioClient):
        self._client = client

    def _post(
        self,
        url: str,
        body: Dict[str, Any],
        files: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return self._client.execute_http_request(
            method="POST",
            url=url,
            params=body or {},
            files=files,
        )

    def _get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._client.execute_http_request(method="GET", url=url, params=params or {})

    def _put(self, url: str, body: Dict[str, Any] = None) -> Dict[str, Any]:
        return self._client.execute_http_request(method="PUT", url=url, params=body or {})

    def _delete(self, url: str) -> Dict[str, Any]:
        return self._client.execute_http_request(
            method="DELETE",
            url=url,
        )
