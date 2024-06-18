import json
import os
from abc import ABC
from functools import cache
from typing import Dict, Optional, TypeVar, Union, Any

import httpx

from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import boto3

from ai21 import AI21APIError
from ai21.errors import AccessDenied, NotFound, APITimeoutError, ModelStreamError
from ai21.http_client.async_http_client import AsyncHttpClient
from ai21.http_client.http_client import HttpClient

_HttpClientT = TypeVar("_HttpClientT", bound=Union[HttpClient, AsyncHttpClient])


_DEFAULT_AWS_REGION = "us-east-1"


class BaseBedrockHttpClient(ABC):
    _http_client: Optional[_HttpClientT] = None

    def __init__(
        self,
        model_id: Optional[str] = None,
        aws_secret_key: Optional[str] = None,
        aws_access_key: Optional[str] = None,
        aws_region: Optional[str] = None,
        aws_session_token: Optional[str] = None,
    ):
        self._model_id = model_id
        self._aws_secret_key = aws_secret_key
        self._aws_access_key = aws_access_key
        self._aws_session_token = aws_session_token

        self._aws_region = aws_region or os.environ.get("AWS_REGION") or _DEFAULT_AWS_REGION

    @cache
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
        data: Optional[str],
    ) -> Dict[str, str]:
        session = self._get_session()
        request = AWSRequest(method="POST", url=url, data=data)
        credentials = session.get_credentials()

        signer = SigV4Auth(credentials, "bedrock", session.region_name)
        signer.add_auth(request)

        prepped = request.prepare()

        return {key: value for key, value in dict(prepped.headers).items() if value is not None}

    def _handle_bedrock_error(self, bedrock_error: AI21APIError) -> None:
        status_code = bedrock_error.status_code
        if status_code == 403:
            raise AccessDenied(details=bedrock_error.details)

        if status_code == 404:
            raise NotFound(details=bedrock_error.details)

        if status_code == 408:
            raise APITimeoutError(details=bedrock_error.details)

        if status_code == 424:
            raise ModelStreamError(details=bedrock_error.details)

    def _build_headers(self, passed_headers: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        headers = {
            "Content-Type": "application/json",
        }

        if passed_headers is not None:
            headers.update(passed_headers)

        return headers


class BedrockHttpClient(BaseBedrockHttpClient):
    def __init__(
        self,
        model_id: Optional[str] = None,
        base_url: Optional[str] = None,
        aws_secret_key: Optional[str] = None,
        aws_access_key: Optional[str] = None,
        aws_region: Optional[str] = None,
        aws_session_token: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout_sec: Optional[int] = None,
        num_retries: Optional[int] = None,
        http_client: Optional[HttpClient] = None,
    ):
        BaseBedrockHttpClient.__init__(
            self,
            model_id=model_id,
            aws_secret_key=aws_secret_key,
            aws_access_key=aws_access_key,
            aws_region=aws_region,
            aws_session_token=aws_session_token,
        )

        if not base_url:
            base_url = f"https://bedrock-runtime.{self._aws_region}.amazonaws.com/model/{self._model_id}/invoke"
        self._base_url = base_url

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
        model_id: str,
        body: Optional[Dict] = None,
    ) -> httpx.Response:
        self._model_id = model_id
        auth_headers = self._prepare_auth_headers(url=self._base_url, data=json.dumps(body))
        try:
            return self._http_client.execute_http_request(
                method="POST",
                url=self._base_url,
                body=body,
                extra_headers=auth_headers,
            )
        except AI21APIError as bedrock_error:
            self._handle_bedrock_error(bedrock_error)
