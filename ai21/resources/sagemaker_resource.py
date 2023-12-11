from __future__ import annotations

import json
from abc import ABC
from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from ai21.clients.sagemaker.ai21_sagemaker_client import AI21SageMakerClient


class SageMakerResource(ABC):
    def __init__(self, sagemaker_client: AI21SageMakerClient):
        self._sagemaker_client = sagemaker_client

    def _invoke(self, body: Dict[str, Any]) -> Dict[str, Any]:
        return self._sagemaker_client.invoke_endpoint(
            input_json=json.dumps(body),
        )
