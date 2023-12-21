import pytest
from pytest_mock import MockerFixture

from ai21 import SageMaker
from ai21.ai21_http_client import AI21HTTPClient
from unittest.mock import patch


@pytest.fixture
def mock_ai21_studio_client(mocker: MockerFixture):
    return mocker.patch.object(
        AI21HTTPClient,
        "execute_http_request",
        return_value={
            "arn": "some-model-package-id1",
            "versions": ["1.0.0", "1.0.1"],
        },
    )


class TestSageMakerService:
    def test__get_model_package_arn__should_return_model_package_arn(self, mocker, mock_ai21_studio_client):
        with patch("ai21.ai21_studio_client.AI21StudioClient"):
            expected_model_package_arn = "some-model-package-id1"

            actual_model_package_arn = SageMaker.get_model_package_arn(model_name="j2-mid", region="us-east-1")

            assert actual_model_package_arn == expected_model_package_arn
