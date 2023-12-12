import json
import re
from typing import Optional, Any, Dict

import boto3
from botocore.exceptions import ClientError

from ai21.ai21_env_config import _AI21EnvConfig, AI21EnvConfig
from ai21.ai21_studio_client import AI21StudioClient
from ai21.clients.sagemaker import resources
from ai21.errors import BadRequest, ServiceUnavailable, ServerError, APIError
from ai21.http_client import handle_non_success_response
from ai21.utils import log_error

__all__ = ["resources", "AI21SageMakerClient"]

# Each one of the clients should be able to implement async/sync interface
_ERROR_MSG_TEMPLATE = (
    r"Received client error \((.*?)\) from primary with message \"(.*?)\". "
    r"See .* in account .* for more information."
)


class AI21SageMakerClient(AI21StudioClient):
    """
    :param endpoint_name: The name of the endpoint to use for the client.
    :param region: The AWS region of the endpoint.
    :param session: An optional boto3 session to use for the client.
    """

    def __init__(
        self,
        endpoint_name: str,
        region: Optional[str] = None,
        session: Optional[boto3.Session] = None,
        api_key: str = None,
        api_host: str = None,
        auth_required: bool = False,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        env_config: _AI21EnvConfig = AI21EnvConfig,
        **kwargs,
    ):
        super().__init__(
            api_key=api_key,
            api_host=api_host,
            auth_required=auth_required,
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
        )
        self._env_config = env_config
        self._session = (
            session if session else boto3.client("sagemaker-runtime", region_name=self._env_config.aws_region)
        )
        self._region = region or self._env_config.aws_region
        self._endpoint_name = endpoint_name
        self.completion = resources.SageMakerCompletion(self)
        self.paraphrase = resources.SageMakerParaphrase(self)
        self.answer = resources.SageMakerAnswer(self)
        self.gec = resources.SageMakerGEC(self)
        self.summarize = resources.SageMakerSummarize(self)

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
            log_error(f"Calling {self._endpoint_name} failed with Exception: {exception}")
            raise exception

    def _handle_client_error(self, client_exception: ClientError):
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
            raise ServerError(details=error_message)
        raise APIError(status_code, details=error_message)

    @property
    def endpoint_name(self) -> str:
        return self._endpoint_name

    @property
    def session(self):
        return self._session
