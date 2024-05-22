import os

import pytest

from ai21 import SageMaker


def _add_or_remove_api_key(use_api_key: bool):
    if use_api_key:
        os.environ["AI21_API_KEY"] = "test"
    else:
        del os.environ["AI21_API_KEY"]


@pytest.mark.parametrize(
    argnames="use_api_key",
    argvalues=[True, False],
    ids=["with_api_key", "without_api_key"],
)
def test_sagemaker__get_model_package_arn(use_api_key: bool):
    _add_or_remove_api_key(use_api_key)
    model_packages_arn = SageMaker.get_model_package_arn(model_name="j2-mid", region="us-east-1")
    assert isinstance(model_packages_arn, str)
    assert len(model_packages_arn) > 0


@pytest.mark.parametrize(
    argnames="use_api_key",
    argvalues=[True, False],
    ids=["with_api_key", "without_api_key"],
)
def test_sagemaker__list_model_package_versions(use_api_key: bool):
    _add_or_remove_api_key(use_api_key)
    model_packages_arn = SageMaker.list_model_package_versions(model_name="j2-mid", region="us-east-1")
    assert isinstance(model_packages_arn, list)
    assert len(model_packages_arn) > 0
