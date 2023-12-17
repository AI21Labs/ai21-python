from typing import Optional

import boto3

from ai21.ai21_env_config import _AI21EnvConfig, AI21EnvConfig
from ai21.clients.sagemaker.resources.sagemaker_answer import SageMakerAnswer
from ai21.clients.sagemaker.resources.sagemaker_completion import SageMakerCompletion
from ai21.clients.sagemaker.resources.sagemaker_gec import SageMakerGEC
from ai21.clients.sagemaker.resources.sagemaker_paraphrase import SageMakerParaphrase
from ai21.clients.sagemaker.resources.sagemaker_summarize import SageMakerSummarize
from ai21.clients.sagemaker.sagemaker_session import SageMakerSession


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
        **kwargs,
    ):

        self._env_config = env_config
        _session = ()
        self._session = SageMakerSession(
            session=session, region=region or self._env_config.aws_region, endpoint_name=endpoint_name
        )
        self.completion = SageMakerCompletion(self._session)
        self.paraphrase = SageMakerParaphrase(self._session)
        self.answer = SageMakerAnswer(self._session)
        self.gec = SageMakerGEC(self._session)
        self.summarize = SageMakerSummarize(self._session)
