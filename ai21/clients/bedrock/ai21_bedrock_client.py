import json
import logging
import warnings
from typing import Optional, Dict, Any

import boto3
import httpx

from ai21 import AI21APIError
from ai21.ai21_env_config import AI21EnvConfig
from ai21.clients.aws.aws_authorization import AWSAuthorization
from ai21.clients.studio.resources.studio_chat import StudioChat, AsyncStudioChat
from ai21.clients.studio.resources.studio_completion import StudioCompletion, AsyncStudioCompletion
from ai21.errors import AccessDenied, NotFound, APITimeoutError, ModelErrorException
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient

_logger = logging.getLogger(__name__)


_BEDROCK_URL_FORMAT = "https://bedrock-runtime.{region}.amazonaws.com"


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


class BaseBedrockClient:
    def __init__(self, session, region):
        self._aws_auth = AWSAuthorization(aws_session=session or boto3.Session(region_name=region))

    def _prepare_options(self, options: Dict[str, Any]) -> Dict[str, Any]:
        body = options.pop("body")
        model = body.pop("model", None)
        stream = body.pop("stream", False)
        url = options["url"]

        if stream:
            _logger.warning("Field stream is not supported. Ignoring it.")

        # When stream is supported we would need to update this section and the URL
        options["url"] = f"{url}/model/{model}/invoke"
        options["body"] = body
        options["headers"] = self._prepare_headers(options)
        return options

    def _prepare_headers(self, options: dict) -> dict:
        body = options.get("body")
        return self._aws_auth.get_auth_headers(
            service_name="bedrock", method="POST", url=options.get("url"), data=json.dumps(body)
        )


class AI21BedrockClient(AI21HTTPClient, BaseBedrockClient):
    def __init__(
        self,
        model_id: Optional[str] = None,
        base_url: Optional[str] = None,
        region: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        session: Optional[boto3.Session] = None,
    ):
        if model_id is not None:
            warnings.warn(
                "Please consider using the 'model_id' parameter in the "
                "'create' method calls instead of the constructor.",
                DeprecationWarning,
            )
        self._region = region or AI21EnvConfig.aws_region
        if base_url is None:
            base_url = _BEDROCK_URL_FORMAT.format(region=self._region)

        AI21HTTPClient.__init__(
            self,
            base_url=base_url,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            headers=headers,
        )

        BaseBedrockClient.__init__(self, session=session, region=self._region)

        self.chat = StudioChat(self)
        # Override the chat.create method to match the completions endpoint,
        # so it wouldn't get to the old J2 completion endpoint
        self.chat.create = self.chat.completions.create
        self.completion = StudioCompletion(self)

    def _build_request(self, options: Dict[str, Any]) -> httpx.Request:
        options = self._prepare_options(options)

        return super()._build_request(options)


class AsyncAI21BedrockClient(AsyncAI21HTTPClient, BaseBedrockClient):
    def __init__(
        self,
        model_id: Optional[str] = None,
        base_url: Optional[str] = None,
        region: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        session: Optional[boto3.Session] = None,
    ):
        if model_id is not None:
            warnings.warn(
                "Please consider using the 'model_id' parameter in the "
                "'create' method calls instead of the constructor.",
                DeprecationWarning,
            )
        self._region = region or AI21EnvConfig.aws_region
        if base_url is None:
            base_url = _BEDROCK_URL_FORMAT.format(region=self._region)

        AsyncAI21HTTPClient.__init__(
            self,
            base_url=base_url,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            headers=headers,
        )

        BaseBedrockClient.__init__(self, session=session, region=self._region)

        self.chat = AsyncStudioChat(self)
        # Override the chat.create method to match the completions endpoint,
        # so it wouldn't get to the old J2 completion endpoint
        self.chat.create = self.chat.completions.create
        self.completion = AsyncStudioCompletion(self)

    def _build_request(self, options: Dict[str, Any]) -> httpx.Request:
        options = self._prepare_options(options)

        return super()._build_request(options)
