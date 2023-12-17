from typing import List

from ai21.ai21_studio_client import AI21StudioClient
from ai21.clients.sagemaker.constants import (
    SAGEMAKER_MODEL_PACKAGE_NAMES,
)
from ai21.errors import ModelPackageDoesntExistException

_JUMPSTART_ENDPOINT = "jumpstart"
_LIST_VERSIONS_ENDPOINT = f"{_JUMPSTART_ENDPOINT}/list_versions"
_GET_ARN_ENDPOINT = f"{_JUMPSTART_ENDPOINT}/get_model_version_arn"

LATEST_VERSION_STR = "latest"


class SageMaker:
    @classmethod
    def get_model_package_arn(cls, model_name: str, region: str, version: str = LATEST_VERSION_STR) -> str:
        _assert_model_package_exists(model_name=model_name, region=region)

        client = AI21StudioClient()

        response = client.execute_http_request(
            method="POST",
            url=f"{client.get_base_url()}/{_GET_ARN_ENDPOINT}",
            params={
                "modelName": model_name,
                "region": region,
                "version": version,
            },
        )

        arn = response["arn"]

        if not arn:
            raise ModelPackageDoesntExistException(model_name=model_name, region=region, version=version)

        return arn

    @classmethod
    def list_model_package_versions(cls, model_name: str, region: str) -> List[str]:
        _assert_model_package_exists(model_name=model_name, region=region)
        client = AI21StudioClient()

        response = client.execute_http_request(
            method="POST",
            url=f"{client.get_base_url()}/{_LIST_VERSIONS_ENDPOINT}",
            params={
                "modelName": model_name,
                "region": region,
            },
        )

        return response["versions"]


def _assert_model_package_exists(model_name, region):
    if model_name not in SAGEMAKER_MODEL_PACKAGE_NAMES:
        raise ModelPackageDoesntExistException(model_name=model_name, region=region)
