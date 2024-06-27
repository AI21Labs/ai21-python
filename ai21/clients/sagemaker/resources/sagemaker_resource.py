from __future__ import annotations

import json
from abc import ABC
from typing import Any, Dict, Optional

import boto3
import httpx

from ai21 import AI21APIError
from ai21.clients.aws.aws_authorization import AWSAuthorization
from ai21.errors import AccessDenied, NotFound, APITimeoutError, ModelErrorException, InternalDependencyException
from ai21.http_client.async_http_client import AsyncHttpClient
from ai21.http_client.http_client import HttpClient


def _handle_sagemaker_error(aws_error: AI21APIError) -> None:
    status_code = aws_error.status_code
    if status_code == 403:
        raise AccessDenied(details=aws_error.details)

    if status_code == 404:
        raise NotFound(details=aws_error.details)

    if status_code == 408:
        raise APITimeoutError(details=aws_error.details)

    if status_code == 424:
        raise ModelErrorException(details=aws_error.details)

    if status_code == 530:
        raise InternalDependencyException(details=aws_error.details)

    raise aws_error


class SageMakerResource(ABC):
    def __init__(
        self,
        endpoint_name: str,
        region: str,
        client: HttpClient,
        aws_session: Optional[boto3.Session] = None,
    ):
        self._client = client
        self._aws_session = aws_session or boto3.Session(region_name=region)
        self._url = f"https://runtime.sagemaker.{region}.amazonaws.com/endpoints/{endpoint_name}/invocations"
        self._aws_auth = AWSAuthorization(aws_session=self._aws_session)

    def _post(
        self,
        body: Dict[str, Any],
    ) -> httpx.Response:
        auth_headers = self._aws_auth.get_auth_headers(
            service_name="sagemaker", url=self._url, method="POST", data=json.dumps(body)
        )

        try:
            return self._client.execute_http_request(
                url=self._url, body=body, method="POST", extra_headers=auth_headers
            )
        except AI21APIError as aws_error:
            _handle_sagemaker_error(aws_error)


class AsyncSageMakerResource(ABC):
    def __init__(
        self,
        endpoint_name: str,
        region: str,
        client: AsyncHttpClient,
        aws_session: Optional[boto3.Session] = None,
    ):
        self._client = client
        self._aws_session = aws_session or boto3.Session(region_name=region)
        self._url = f"https://runtime.sagemaker.{region}.amazonaws.com/endpoints/{endpoint_name}/invocations"
        self._aws_auth = AWSAuthorization(aws_session=self._aws_session)

    async def _post(
        self,
        body: Dict[str, Any],
    ) -> httpx.Response:
        auth_headers = self._aws_auth.get_auth_headers(
            service_name="sagemaker", url=self._url, method="POST", data=json.dumps(body)
        )

        try:
            return await self._client.execute_http_request(
                url=self._url, body=body, method="POST", extra_headers=auth_headers
            )
        except AI21APIError as aws_error:
            _handle_sagemaker_error(aws_error)
