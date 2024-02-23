import json
from abc import ABC
from typing import Any, Dict

from ai21.clients.bedrock.bedrock_session import BedrockSession


class BedrockResource(ABC):
    def __init__(self, model_id: str, bedrock_session: BedrockSession):
        self._model_id = model_id
        self._bedrock_session = bedrock_session

    def _invoke(self, model_id: str, body: Dict[str, Any]) -> Dict[str, Any]:
        return self._bedrock_session.invoke_model(
            input_json=json.dumps(body),
            model_id=model_id,
        )
