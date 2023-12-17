from ai21 import SageMaker

print(SageMaker.list_model_package_versions(model_name="j2-mid", region="us-east-1"))
print(SageMaker.get_model_package_arn(model_name="j2-mid", region="us-east-1"))
