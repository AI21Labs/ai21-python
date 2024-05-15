import httpx
import pytest

from ai21 import ModelPackageDoesntExistError
from tests.unittests.services.sagemaker_stub import SageMakerStub

_DUMMY_ARN = "some-model-package-id1"
_DUMMY_VERSIONS = ["1.0.0", "1.0.1"]


class TestSageMakerService:
    def test__get_model_package_arn__should_return_model_package_arn(self, mock_httpx_response: httpx.Response):
        mock_httpx_response.json.return_value = {
            "arn": _DUMMY_ARN,
            "versions": _DUMMY_VERSIONS,
        }
        SageMakerStub.ai21_http_client.execute_http_request.return_value = mock_httpx_response

        actual_model_package_arn = SageMakerStub.get_model_package_arn(model_name="j2-mid", region="us-east-1")

        assert actual_model_package_arn == _DUMMY_ARN

    def test__get_model_package_arn__when_no_arn__should_raise_error(self, mock_httpx_response: httpx.Response):
        mock_httpx_response.json.return_value = {"arn": []}
        SageMakerStub.ai21_http_client.execute_http_request.return_value = mock_httpx_response

        with pytest.raises(ModelPackageDoesntExistError):
            SageMakerStub.get_model_package_arn(model_name="j2-mid", region="us-east-1")

    def test__list_model_package_versions__should_return_model_package_arn(self, mock_httpx_response: httpx.Response):
        mock_httpx_response.json.return_value = {
            "versions": _DUMMY_VERSIONS,
        }
        SageMakerStub.ai21_http_client.execute_http_request.return_value = mock_httpx_response

        actual_model_package_arn = SageMakerStub.list_model_package_versions(model_name="j2-mid", region="us-east-1")

        assert actual_model_package_arn == _DUMMY_VERSIONS

    def test__list_model_package_versions__when_model_package_not_available__should_raise_an_error(self):
        with pytest.raises(ModelPackageDoesntExistError):
            SageMakerStub.list_model_package_versions(model_name="openai", region="us-east-1")

    def test__get_model_package_arn__when_model_package_not_available__should_raise_an_error(self):
        with pytest.raises(ModelPackageDoesntExistError):
            SageMakerStub.get_model_package_arn(model_name="openai", region="us-east-1")
