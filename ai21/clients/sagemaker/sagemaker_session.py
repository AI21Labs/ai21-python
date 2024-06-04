import json
import re

import boto3
from botocore.exceptions import ClientError

from ai21.errors import BadRequest, ServiceUnavailable, AI21ServerError, AI21APIError
from ai21.http_client.base_http_client import handle_non_success_response
from ai21.logger import logger

_ERROR_MSG_TEMPLATE = (
    r"Received client error \((.*?)\) from primary with message \"(.*?)\". "
    r"See .* in account .* for more information."
)
_SAGEMAKER_RUNTIME_NAME = "sagemaker-runtime"


class SageMakerSession:
    def __init__(self, session: boto3.Session, region: str, endpoint_name: str):
        self._session = session if session else boto3.client(_SAGEMAKER_RUNTIME_NAME, region_name=region)
        self._region = region
        self._endpoint_name = endpoint_name

    def invoke_endpoint(
        self,
        input_json: str,
    ):
        try:
            response = self._session.invoke_endpoint(
                EndpointName=self._endpoint_name,
                ContentType="application/json",
                Accept="application/json",
                Body=input_json,
            )

            return json.load(response["Body"])
        except ClientError as sm_client_error:
            self._handle_client_error(sm_client_error)
        except Exception as exception:
            logger.error(f"Calling {self._endpoint_name} failed with Exception: {exception}")
            raise exception

    def _handle_client_error(self, client_exception: "ClientError"):
        error_response = client_exception.response
        error_message = error_response.get("Error", {}).get("Message", "")
        status_code = error_response.get("ResponseMetadata", {}).get("HTTPStatusCode", None)
        # According to https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html#API_runtime_InvokeEndpoint_Errors
        if status_code == 400:
            raise BadRequest(details=error_message)
        if status_code == 424:
            error_message_template = re.compile(_ERROR_MSG_TEMPLATE)
            model_status_code = int(error_message_template.search(error_message).group(1))
            model_error_message = error_message_template.search(error_message).group(2)
            handle_non_success_response(model_status_code, model_error_message)
        if status_code == 429 or status_code == 503:
            raise ServiceUnavailable(details=error_message)
        if status_code == 500:
            raise AI21ServerError(details=error_message)
        raise AI21APIError(status_code, details=error_message)
