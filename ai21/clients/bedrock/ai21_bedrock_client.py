from typing import Optional

import boto3

from ai21.ai21_env_config import AI21EnvConfig, _AI21EnvConfig
from ai21.clients.bedrock.bedrock_session import BedrockSession
from ai21.clients.bedrock.resources.bedrock_completion import BedrockCompletion

_RUNTIME_NAME = "bedrock-runtime"


class AI21BedrockClient:
    """
    :param session: An optional boto3 session to use for the client.
    """

    def __init__(
        self,
        session: Optional[boto3.Session] = None,
        env_config: _AI21EnvConfig = AI21EnvConfig,
    ):

        bedrock_session = (
            session.client(_RUNTIME_NAME) if session else boto3.client(_RUNTIME_NAME, region_name=env_config.aws_region)
        )
        self._bedrock_session = BedrockSession(bedrock_session)
        self.completion = BedrockCompletion(self._bedrock_session)
