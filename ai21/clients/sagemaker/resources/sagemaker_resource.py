from __future__ import annotations

from abc import ABC
from typing import Any, Dict

import httpx

from ai21.clients.aws_http_client.aws_http_client import AWSHttpClient


class SageMakerResource(ABC):
    def __init__(
        self,
        endpoint_name: str,
        region: str,
        client: AWSHttpClient,
    ):
        self._client = client

        self._url = f"https://runtime.sagemaker.{region}.amazonaws.com/endpoints/{endpoint_name}/invocations"

    def _post(
        self,
        body: Dict[str, Any],
    ) -> httpx.Response:
        return self._client.execute_http_request(url=self._url, body=body, method="POST", service_name="sagemaker")
