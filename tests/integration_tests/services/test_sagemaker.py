import pytest

from ai21 import SageMaker
from tests.integration_tests.skip_helpers import should_skip_studio_integration_tests


@pytest.mark.skipif(should_skip_studio_integration_tests(), reason="No key supplied for AI21 Studio. Skipping.")
def test_sagemker__get_model_package_arn():
    model_packages_arn = SageMaker.get_model_package_arn(model_name="j2-mid", region="us-east-1")
    assert isinstance(model_packages_arn, str)
    assert len(model_packages_arn) > 0


@pytest.mark.skipif(should_skip_studio_integration_tests(), reason="No key supplied for AI21 Studio. Skipping.")
def test_sagemker__list_model_package_versions():
    model_packages_arn = SageMaker.list_model_package_versions(model_name="j2-mid", region="us-east-1")
    assert isinstance(model_packages_arn, list)
    assert len(model_packages_arn) > 0
