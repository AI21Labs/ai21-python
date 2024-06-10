from typing import List

from ai21 import AI21EnvConfig
from ai21.ai21_http_client.ai21_http_client import AI21HTTPClient
from ai21.clients.sagemaker.constants import (
    SAGEMAKER_MODEL_PACKAGE_NAMES,
)
from ai21.errors import ModelPackageDoesntExistError

_JUMPSTART_ENDPOINT = "jumpstart"
_LIST_VERSIONS_ENDPOINT = f"{_JUMPSTART_ENDPOINT}/list_versions"
_GET_ARN_ENDPOINT = f"{_JUMPSTART_ENDPOINT}/get_model_version_arn"

LATEST_VERSION_STR = "latest"


class SageMaker:
    @classmethod
    def get_model_package_arn(cls, model_name: str, region: str, version: str = LATEST_VERSION_STR) -> str:
        _assert_model_package_exists(model_name=model_name, region=region)

        client = cls._create_ai21_http_client()

        response = client.execute_http_request(
            method="POST",
            path=f"/{_GET_ARN_ENDPOINT}",
            body={
                "modelName": model_name,
                "region": region,
                "version": version,
            },
        )

        arn = response.json()["arn"]

        if not arn:
            raise ModelPackageDoesntExistError(model_name=model_name, region=region, version=version)

        return arn

    @classmethod
    def list_model_package_versions(cls, model_name: str, region: str) -> List[str]:
        _assert_model_package_exists(model_name=model_name, region=region)

        client = cls._create_ai21_http_client()

        response = client.execute_http_request(
            method="POST",
            path=f"/{_LIST_VERSIONS_ENDPOINT}",
            body={
                "modelName": model_name,
                "region": region,
            },
        )

        return response.json()["versions"]

    @classmethod
    def _create_ai21_http_client(cls) -> AI21HTTPClient:
        return AI21HTTPClient(
            api_key=AI21EnvConfig.api_key,
            base_url=f"{AI21EnvConfig.api_host}/studio/v1",
            requires_api_key=False,
            api_version=AI21EnvConfig.api_version,
            timeout_sec=AI21EnvConfig.timeout_sec,
            num_retries=AI21EnvConfig.num_retries,
        )


def _assert_model_package_exists(model_name, region):
    if model_name not in SAGEMAKER_MODEL_PACKAGE_NAMES:
        raise ModelPackageDoesntExistError(model_name=model_name, region=region)
