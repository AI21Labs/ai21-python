from typing import Optional

import boto3

from ai21.ai21_env_config import AI21EnvConfig, _AI21EnvConfig
from ai21.clients.bedrock.bedrock_session import BedrockSession
from ai21.clients.bedrock.resources.bedrock_completion import BedrockCompletion


class AI21BedrockClient:
    """
    :param session: An optional boto3 session to use for the client.
    """

    def __init__(
        self,
        session: Optional[boto3.Session] = None,
        region: Optional[str] = None,
        env_config: _AI21EnvConfig = AI21EnvConfig,
    ):

        self._bedrock_session = BedrockSession(session=session, region=region or env_config.aws_region)
        self.completion = BedrockCompletion(self._bedrock_session)
