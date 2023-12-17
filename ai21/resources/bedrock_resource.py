import json
from abc import ABC
from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from ai21.clients.bedrock.ai21_bedrock_client import AI21BedrockClient


class BedrockResource(ABC):
    def __init__(self, bedrock_client: AI21BedrockClient):
        self._bedrock_client = bedrock_client

    def _invoke(self, model_id: str, body: Dict[str, Any]) -> Dict[str, Any]:
        return self._bedrock_client.invoke_model(
            input_json=json.dumps(body),
            model_id=model_id,
        )
