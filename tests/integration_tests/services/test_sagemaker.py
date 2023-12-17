from ai21 import SageMaker


def test_sagemker__get_model_package_arn():
    model_packages_arn = SageMaker.get_model_package_arn(model_name="j2-mid", region="us-east-1")
    assert isinstance(model_packages_arn, str)
    assert len(model_packages_arn) > 0


def test_sagemker__list_model_package_versions():
    model_packages_arn = SageMaker.list_model_package_versions(model_name="j2-mid", region="us-east-1")
    assert isinstance(model_packages_arn, list)
    assert len(model_packages_arn) > 0
