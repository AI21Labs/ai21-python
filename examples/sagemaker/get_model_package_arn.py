import ai21

print(
    ai21.SageMaker.list_model_package_versions(model_name="j2-mid", region="us-east-1")
)
print(ai21.SageMaker.get_model_package_arn(model_name="j2-mid", region="us-east-1"))
