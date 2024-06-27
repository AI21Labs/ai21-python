from typing import Optional, Dict, Any

import boto3

from ai21.ai21_env_config import _AI21EnvConfig, AI21EnvConfig

from ai21.clients.aws.utils import get_aws_region
from ai21.clients.sagemaker.resources.sagemaker_answer import SageMakerAnswer
from ai21.clients.sagemaker.resources.sagemaker_completion import SageMakerCompletion
from ai21.clients.sagemaker.resources.sagemaker_gec import SageMakerGEC
from ai21.clients.sagemaker.resources.sagemaker_paraphrase import SageMakerParaphrase
from ai21.clients.sagemaker.resources.sagemaker_summarize import SageMakerSummarize
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
        self.completion = SageMakerCompletion(endpoint_name=endpoint_name, region=region, client=self._http_client)
        self.paraphrase = SageMakerParaphrase(endpoint_name=endpoint_name, region=region, client=self._http_client)
        self.answer = SageMakerAnswer(endpoint_name=endpoint_name, region=region, client=self._http_client)
        self.gec = SageMakerGEC(endpoint_name=endpoint_name, region=region, client=self._http_client)
        self.summarize = SageMakerSummarize(endpoint_name=endpoint_name, region=region, client=self._http_client)
