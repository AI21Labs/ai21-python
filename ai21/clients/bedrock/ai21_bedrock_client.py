from typing import Optional, Dict, Any

from ai21.clients.bedrock.bedrock_http_client import BedrockHttpClient
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
    ):
        self._http_client = BedrockHttpClient(
            model_id=model_id,
            aws_region=region,
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            http_client=http_client,
        )

        self.completion = BedrockCompletion(self._http_client)
