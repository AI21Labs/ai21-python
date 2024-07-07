from unittest.mock import Mock

from ai21 import SageMaker
from ai21.http_client.http_client import AI21HTTPClient


class SageMakerStub(SageMaker):
    ai21_http_client = Mock(spec=AI21HTTPClient)

    @classmethod
    def _create_ai21_http_client(cls, path: str) -> AI21HTTPClient:
        return cls.ai21_http_client
