from typing import Optional, Dict, Any

import boto3

from ai21.ai21_env_config import _AI21EnvConfig, AI21EnvConfig

from ai21.clients.aws.utils import get_aws_region
from ai21.clients.sagemaker.resources.sagemaker_answer import SageMakerAnswer, AsyncSageMakerAnswer
from ai21.clients.sagemaker.resources.sagemaker_completion import SageMakerCompletion, AsyncSageMakerCompletion
from ai21.clients.sagemaker.resources.sagemaker_gec import SageMakerGEC, AsyncSageMakerGEC
from ai21.clients.sagemaker.resources.sagemaker_paraphrase import SageMakerParaphrase, AsyncSageMakerParaphrase
from ai21.clients.sagemaker.resources.sagemaker_summarize import SageMakerSummarize, AsyncSageMakerSummarize
from ai21.http_client.async_http_client import AsyncHttpClient
from ai21.http_client.http_client import HttpClient


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
        env_config: _AI21EnvConfig = AI21EnvConfig,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        http_client: Optional[HttpClient] = None,
        **kwargs,
    ):
        region = get_aws_region(env_config=env_config, session=session, region=region)
        self._http_client = http_client or HttpClient(
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
        )

        self.completion = SageMakerCompletion(
            endpoint_name=endpoint_name, region=region, client=self._http_client, aws_session=session
        )
        self.paraphrase = SageMakerParaphrase(
            endpoint_name=endpoint_name, region=region, client=self._http_client, aws_session=session
        )
        self.answer = SageMakerAnswer(
            endpoint_name=endpoint_name, region=region, client=self._http_client, aws_session=session
        )
        self.gec = SageMakerGEC(
            endpoint_name=endpoint_name, region=region, client=self._http_client, aws_session=session
        )
        self.summarize = SageMakerSummarize(
            endpoint_name=endpoint_name, region=region, client=self._http_client, aws_session=session
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
        env_config: _AI21EnvConfig = AI21EnvConfig,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        http_client: Optional[AsyncHttpClient] = None,
        **kwargs,
    ):
        region = get_aws_region(env_config=env_config, session=session, region=region)
        self._http_client = http_client or AsyncHttpClient(
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
        )

        self.completion = AsyncSageMakerCompletion(
            endpoint_name=endpoint_name, region=region, client=self._http_client, aws_session=session
        )
        self.paraphrase = AsyncSageMakerParaphrase(
            endpoint_name=endpoint_name, region=region, client=self._http_client, aws_session=session
        )
        self.answer = AsyncSageMakerAnswer(
            endpoint_name=endpoint_name, region=region, client=self._http_client, aws_session=session
        )
        self.gec = AsyncSageMakerGEC(
            endpoint_name=endpoint_name, region=region, client=self._http_client, aws_session=session
        )
        self.summarize = AsyncSageMakerSummarize(
            endpoint_name=endpoint_name, region=region, client=self._http_client, aws_session=session
        )
