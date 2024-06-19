from __future__ import annotations

from abc import ABC
from typing import Any, Dict, Optional

import httpx

from ai21.clients.aws.aws_http_client import AWSHttpClient


class BedrockResource(ABC):
    def __init__(
        self,
        region: str,
        client: AWSHttpClient,
        model_id: Optional[str] = None,
    ):
        self._region = region
        self._model_id = model_id
        self._client = client

    def _post(
        self,
        body: Dict[str, Any],
        model_id: str,
    ) -> httpx.Response:
        url = self._build_url(model_id=model_id)
        return self._client.execute_http_request(url=url, body=body, method="POST", service_name="bedrock")

    def _build_url(self, model_id: str) -> str:
        return f"https://bedrock-runtime.{self._region}.amazonaws.com/model/{model_id}/invoke"
