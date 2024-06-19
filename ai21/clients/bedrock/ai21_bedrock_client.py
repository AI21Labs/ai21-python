from typing import Optional, Dict, Any

import boto3

from ai21.clients.aws.aws_http_client import AWSHttpClient, DEFAULT_AWS_REGION
from ai21.clients.bedrock.resources.bedrock_completion import BedrockCompletion
from ai21.http_client.http_client import HttpClient


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
    ):
        self._model_id = model_id
        self._bedrock_session = session
        region = session.region_name if session is not None else region or DEFAULT_AWS_REGION
        self._http_client = AWSHttpClient(
            aws_region=region,
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            http_client=http_client,
            aws_session=session,
        )

        self.completion = BedrockCompletion(model_id=model_id, region=region, client=self._http_client)
