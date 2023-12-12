import sagemaker as sage
import boto3
from sagemaker import ModelPackage

b_session = boto3.Session(profile_name="default")
s_session = sage.Session(boto_session=boto3.Session(profile_name="default"))

role = "role"
region = boto3.Session().region_name
model_name = "model_name"
content_type = "application/json"
real_time_inference_instance_type = "ml.g5.48xlarge"
model_package_arn = "package_arn"
model = ModelPackage(role=role, model_package_arn=model_package_arn, sagemaker_session=s_session)
model.deploy(
    1,
    real_time_inference_instance_type,
    endpoint_name=model_name,
    model_data_download_timeout=3600,
    container_startup_health_check_timeout=600,
)

print("finished deploying model")
