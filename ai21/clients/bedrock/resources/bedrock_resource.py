from __future__ import annotations

from abc import ABC
from typing import Any, Dict, Optional

import httpx

from ai21.clients.bedrock.bedrock_http_client import BedrockHttpClient


class BedrockResource(ABC):
    def __init__(self, client: BedrockHttpClient, model_id: Optional[str] = None):
        self._client = client
        self._model_id = model_id

    def _post(
        self,
        model_id: str,
        body: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        return self._client.execute_http_request(
            model_id=model_id,
            body=body,
        )
