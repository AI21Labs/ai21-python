import warnings
from typing import Optional, Dict, Any

import boto3

from ai21.ai21_env_config import _AI21EnvConfig, AI21EnvConfig
from ai21.clients.bedrock.resources.chat.bedrock_chat import BedrockChat, AsyncBedrockChat
from ai21.clients.bedrock.resources.bedrock_completion import BedrockCompletion, AsyncBedrockCompletion
from ai21.http_client.http_client import HttpClient
from ai21.http_client.async_http_client import AsyncHttpClient


def _get_aws_region(
    env_config: _AI21EnvConfig,
    session: Optional[boto3.Session] = None,
    region: Optional[str] = None,
) -> str:
    if session is not None:
        return session.region_name

    return region or env_config.aws_region


class AI21BedrockClient:
    def __init__(
        self,
        model_id: Optional[str] = None,
        region: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        http_client: Optional[HttpClient] = None,
        session: Optional[boto3.Session] = None,
        env_config: _AI21EnvConfig = AI21EnvConfig,
    ):
        if model_id is not None:
            warnings.warn(
                "Please consider using the 'model_id' parameter in the "
                "'create' method calls instead of the constructor.",
                DeprecationWarning,
            )

        region = _get_aws_region(env_config=env_config, session=session, region=region)

        self._http_client = http_client or HttpClient(
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            headers=headers,
        )

        self.completion = BedrockCompletion(
            model_id=model_id, region=region, client=self._http_client, aws_session=session
        )
        self.chat = BedrockChat(model_id=model_id, region=region, client=self._http_client, aws_session=session)


class AsyncAI21BedrockClient:
    def __init__(
        self,
        model_id: Optional[str] = None,
        region: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        http_client: Optional[AsyncHttpClient] = None,
        session: Optional[boto3.Session] = None,
        env_config: _AI21EnvConfig = AI21EnvConfig,
    ):
        region = _get_aws_region(env_config=env_config, session=session, region=region)

        self._http_client = http_client or AsyncHttpClient(
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            headers=headers,
        )

        self.completion = AsyncBedrockCompletion(model_id=model_id, region=region, client=self._http_client)
        self.chat = AsyncBedrockChat(model_id=model_id, region=region, client=self._http_client, aws_session=session)
