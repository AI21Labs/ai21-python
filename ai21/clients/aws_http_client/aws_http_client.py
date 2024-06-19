import json
from abc import ABC
from functools import lru_cache
from typing import Dict, Optional, TypeVar, Union, Any

import httpx

from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import boto3

from ai21 import AI21APIError
from ai21.errors import (
    AccessDenied,
    NotFound,
    APITimeoutError,
    ModelStreamError,
    BadRequest,
    AI21ServerError,
)
from ai21.http_client.async_http_client import AsyncHttpClient
from ai21.http_client.http_client import HttpClient

_HttpClientT = TypeVar("_HttpClientT", bound=Union[HttpClient, AsyncHttpClient])


DEFAULT_AWS_REGION = "us-east-1"


class BaseAWSHttpClient(ABC):
    _http_client: Optional[_HttpClientT] = None

    def __init__(
        self,
        aws_secret_key: Optional[str] = None,
        aws_access_key: Optional[str] = None,
        aws_region: Optional[str] = None,
        aws_session_token: Optional[str] = None,
        aws_session: Optional[boto3.Session] = None,
    ):
        self._aws_secret_key = aws_secret_key
        self._aws_access_key = aws_access_key
        self._aws_session_token = aws_session_token
        self._aws_session = aws_session

        self._aws_region = aws_region or DEFAULT_AWS_REGION

    @lru_cache(maxsize=None)
    def _get_session(self) -> boto3.Session:
        return boto3.Session(
            region_name=self._aws_region,
            aws_access_key_id=self._aws_access_key,
            aws_secret_access_key=self._aws_secret_key,
            aws_session_token=self._aws_session_token,
        )

    def _prepare_auth_headers(
        self,
        *,
        url: str,
        service_name: str,
        method: str,
        data: Optional[str],
    ) -> Dict[str, str]:
        if self._aws_session is None:
            self._aws_session = self._get_session()
        request = AWSRequest(method=method, url=url, data=data)
        credentials = self._aws_session.get_credentials()

        signer = SigV4Auth(
            credentials=credentials, service_name=service_name, region_name=self._aws_session.region_name
        )
        signer.add_auth(request)

        prepped = request.prepare()

        return {key: value for key, value in dict(prepped.headers).items() if value is not None}

    def _handle_aws_error(self, aws_error: AI21APIError) -> None:
        status_code = aws_error.status_code
        if status_code == 400:
            raise BadRequest(details=aws_error.details)
        if status_code == 403:
            raise AccessDenied(details=aws_error.details)
        if status_code == 404:
            raise NotFound(details=aws_error.details)
        if status_code == 408:
            raise APITimeoutError(details=aws_error.details)
        if status_code == 424:
            raise ModelStreamError(details=aws_error.details)
        if status_code == 500:
            raise AI21ServerError(details=aws_error.details)
        raise AI21APIError(status_code, details=aws_error.details)

    def _build_headers(self, passed_headers: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        headers = {
            "Content-Type": "application/json",
        }

        if passed_headers is not None:
            headers.update(passed_headers)

        return headers


class AWSHttpClient(BaseAWSHttpClient):
    def __init__(
        self,
        aws_secret_key: Optional[str] = None,
        aws_access_key: Optional[str] = None,
        aws_region: Optional[str] = None,
        aws_session_token: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout_sec: Optional[int] = None,
        num_retries: Optional[int] = None,
        http_client: Optional[HttpClient] = None,
        aws_session: Optional[boto3.Session] = None,
    ):
        BaseAWSHttpClient.__init__(
            self,
            aws_secret_key=aws_secret_key,
            aws_access_key=aws_access_key,
            aws_region=aws_region,
            aws_session_token=aws_session_token,
            aws_session=aws_session,
        )

        headers = self._build_headers(passed_headers=headers)
        self._http_client = self._init_http_client(
            http_client=http_client, headers=headers, timeout_sec=timeout_sec, num_retries=num_retries
        )

    def _init_http_client(
        self,
        http_client: Optional[HttpClient],
        headers: Dict[str, Any],
        timeout_sec: Optional[int],
        num_retries: Optional[int],
    ) -> HttpClient:
        if http_client is None:
            return HttpClient(
                timeout_sec=timeout_sec,
                num_retries=num_retries,
                headers=headers,
            )

        http_client.add_headers(headers)

        return http_client

    def execute_http_request(
        self,
        method: str,
        service_name: str,
        url: str,
        body: Optional[Dict] = None,
    ) -> httpx.Response:
        auth_headers = self._prepare_auth_headers(
            url=url, data=json.dumps(body), service_name=service_name, method=method
        )

        try:
            return self._http_client.execute_http_request(
                method=method,
                url=url,
                body=body,
                extra_headers=auth_headers,
            )
        except AI21APIError as aws_error:
            self._handle_aws_error(aws_error)


class AsyncAWSHttpClient(BaseAWSHttpClient):
    def __init__(
        self,
        aws_secret_key: Optional[str] = None,
        aws_access_key: Optional[str] = None,
        aws_region: Optional[str] = None,
        aws_session_token: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout_sec: Optional[int] = None,
        num_retries: Optional[int] = None,
        http_client: Optional[AsyncHttpClient] = None,
        aws_session: Optional[boto3.Session] = None,
    ):
        BaseAWSHttpClient.__init__(
            self,
            aws_secret_key=aws_secret_key,
            aws_access_key=aws_access_key,
            aws_region=aws_region,
            aws_session_token=aws_session_token,
            aws_session=aws_session,
        )

        headers = self._build_headers(passed_headers=headers)
        self._http_client = self._init_http_client(
            http_client=http_client, headers=headers, timeout_sec=timeout_sec, num_retries=num_retries
        )

    def _init_http_client(
        self,
        http_client: Optional[AsyncHttpClient],
        headers: Dict[str, Any],
        timeout_sec: Optional[int],
        num_retries: Optional[int],
    ) -> AsyncHttpClient:
        if http_client is None:
            return AsyncHttpClient(
                timeout_sec=timeout_sec,
                num_retries=num_retries,
                headers=headers,
            )

        http_client.add_headers(headers)

        return http_client

    async def execute_http_request(
        self,
        method: str,
        service_name: str,
        url: str,
        body: Optional[Dict] = None,
    ) -> httpx.Response:
        auth_headers = self._prepare_auth_headers(
            url=url, data=json.dumps(body), service_name=service_name, method=method
        )

        try:
            return await self._http_client.execute_http_request(
                method=method,
                url=url,
                body=body,
                extra_headers=auth_headers,
            )
        except AI21APIError as aws_error:
            self._handle_aws_error(aws_error)
