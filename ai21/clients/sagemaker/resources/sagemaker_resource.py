from __future__ import annotations

import json
from abc import ABC
from typing import Any, Dict

from ai21.clients.sagemaker.sagemaker_session import SageMakerSession


class SageMakerResource(ABC):
    def __init__(self, sagemaker_session: SageMakerSession):
        self._sagemaker_session = sagemaker_session

    def _invoke(self, body: Dict[str, Any]) -> Dict[str, Any]:
        return self._sagemaker_session.invoke_endpoint(
            input_json=json.dumps(body),
        )
