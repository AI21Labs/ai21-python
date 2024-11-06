from typing import Optional, Dict, Any

import boto3

from ai21.ai21_env_config import AI21EnvConfig
from ai21.clients.sagemaker.resources.sagemaker_completion import SageMakerCompletion, AsyncSageMakerCompletion
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient


class AI21SageMakerClient:
    """
    :param endpoint_name: The name of the endpoint to use for the client.
    :param region: The AWS region of the endpoint.
    :param session: An optional boto3 session to use for the client.
    """

    def __init__(
        self,
        endpoint_name: str,
        region: Optional[str] = None,
        session: Optional["boto3.Session"] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        http_client: Optional[AI21HTTPClient] = None,
        **kwargs,
    ):
        region = region or AI21EnvConfig.aws_region
        base_url = f"https://runtime.sagemaker.{region}.amazonaws.com/endpoints/{endpoint_name}/invocations"
        self._http_client = http_client or AI21HTTPClient(
            base_url=base_url,
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            requires_api_key=False,
        )

        self.completion = SageMakerCompletion(
            base_url=base_url, region=region, client=self._http_client, aws_session=session
        )


class AsyncAI21SageMakerClient:
    """
    :param endpoint_name: The name of the endpoint to use for the client.
    :param region: The AWS region of the endpoint.
    :param session: An optional boto3 session to use for the client.
    """

    def __init__(
        self,
        endpoint_name: str,
        region: Optional[str] = None,
        session: Optional["boto3.Session"] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        http_client: Optional[AsyncAI21HTTPClient] = None,
        **kwargs,
    ):
        region = region or AI21EnvConfig.aws_region
        base_url = f"https://runtime.sagemaker.{region}.amazonaws.com/endpoints/{endpoint_name}/invocations"
        self._http_client = http_client or AsyncAI21HTTPClient(
            base_url=base_url,
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            requires_api_key=False,
        )

        self.completion = AsyncSageMakerCompletion(
            base_url=base_url, region=region, client=self._http_client, aws_session=session
        )
