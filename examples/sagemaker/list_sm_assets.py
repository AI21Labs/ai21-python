import sagemaker as sage
import boto3

s = sage.Session(boto_session=boto3.Session(profile_name="default"))

endpoint_results = s.search("Endpoint")
for result in endpoint_results["Results"]:
    print(result)

endpoint_results = s.search("Model")
for result in endpoint_results["Results"]:
    print(result)

m_p_results = s.search("ModelPackage")
for result in m_p_results["Results"]:
    print(result)
