from __future__ import annotations

import json
from abc import ABC
from typing import Any, Dict, Optional

import boto3
import httpx

from ai21 import AI21APIError
from ai21.clients.aws.aws_authorization import AWSAuthorization
from ai21.errors import AccessDenied, NotFound, APITimeoutError, ModelErrorException
from ai21.http_client.async_http_client import AsyncHttpClient
from ai21.http_client.http_client import HttpClient


def _build_url(model_id: str, region: str) -> str:
    return f"https://bedrock-runtime.{region}.amazonaws.com/model/{model_id}/invoke"


def _handle_bedrock_error(aws_error: AI21APIError) -> None:
    status_code = aws_error.status_code
    if status_code == 403:
        raise AccessDenied(details=aws_error.details)

    if status_code == 404:
        raise NotFound(details=aws_error.details)

    if status_code == 408:
        raise APITimeoutError(details=aws_error.details)

    if status_code == 424:
        raise ModelErrorException(details=aws_error.details)

    raise aws_error


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
        url = _build_url(model_id=model_id, region=self._region)
        auth_headers = self._aws_auth.get_auth_headers(
            service_name="bedrock", url=url, method="POST", data=json.dumps(body)
        )

        try:
            return self._client.execute_http_request(url=url, body=body, method="POST", extra_headers=auth_headers)
        except AI21APIError as aws_error:
            _handle_bedrock_error(aws_error)


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
        url = _build_url(model_id=model_id, region=self._region)
        auth_headers = self._aws_auth.get_auth_headers(
            service_name="bedrock", url=url, method="POST", data=json.dumps(body)
        )

        try:
            return await self._client.execute_http_request(
                url=url, body=body, method="POST", extra_headers=auth_headers
            )
        except AI21APIError as aws_error:
            _handle_bedrock_error(aws_error)
