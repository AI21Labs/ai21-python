from __future__ import annotations

import json
from abc import ABC
from typing import Any, Dict, Optional

import boto3
import httpx

from ai21.clients.aws_http_client.aws_authorization import AWSAuthorization
from ai21.http_client.async_http_client import AsyncHttpClient
from ai21.http_client.http_client import HttpClient


class BedrockResource(ABC):
    def __init__(
        self,
        region: str,
        client: HttpClient,
        model_id: Optional[str] = None,
        aws_session: Optional[boto3.Session] = None,
    ):
        self._region = region
        self._model_id = model_id
        self._client = client
        self._aws_session = aws_session or boto3.Session(region_name=region)
        self._aws_auth = AWSAuthorization(aws_session=self._aws_session)

    def _post(
        self,
        body: Dict[str, Any],
        model_id: str,
    ) -> httpx.Response:
        url = self._build_url(model_id=model_id)
        auth_headers = self._aws_auth.prepare_auth_headers(
            service_name="bedrock", url=url, method="POST", data=json.dumps(body)
        )

        return self._client.execute_http_request(url=url, body=body, method="POST", extra_headers=auth_headers)

    def _build_url(self, model_id: str) -> str:
        return f"https://bedrock-runtime.{self._region}.amazonaws.com/model/{model_id}/invoke"


class AsyncBedrockResource(ABC):
    def __init__(
        self,
        region: str,
        client: AsyncHttpClient,
        model_id: Optional[str] = None,
        aws_session: Optional[boto3.Session] = None,
    ):
        self._region = region
        self._model_id = model_id
        self._client = client
        self._aws_session = aws_session or boto3.Session(region_name=region)
        self._aws_auth = AWSAuthorization(aws_session=self._aws_session)

    async def _post(
        self,
        body: Dict[str, Any],
        model_id: str,
    ) -> httpx.Response:
        url = self._build_url(model_id=model_id)
        auth_headers = self._aws_auth.prepare_auth_headers(
            service_name="bedrock", url=url, method="POST", data=json.dumps(body)
        )

        return await self._client.execute_http_request(url=url, body=body, method="POST", extra_headers=auth_headers)

    def _build_url(self, model_id: str) -> str:
        return f"https://bedrock-runtime.{self._region}.amazonaws.com/model/{model_id}/invoke"
