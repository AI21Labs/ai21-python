import json
import re
from typing import Optional, Any, Dict


from ai21.ai21_env_config import AI21EnvConfig, _AI21EnvConfig
from ai21.clients.bedrock.resources.bedrock_completion import BedrockCompletion
from ai21.errors import AccessDenied, NotFound, APITimeoutError
from ai21.http_client import handle_non_success_response
from ai21.utils import log_error

_RUNTIME_NAME = "bedrock-runtime"
_ERROR_MSG_TEMPLATE = (
    r"Received client error \((.*?)\) from primary with message \"(.*?)\". "
    r"See .* in account .* for more information."
)


class AI21BedrockClient:
    """
    :param session: An optional boto3 session to use for the client.
    """

    def __init__(
        self,
        session: Optional["boto3.Session"] = None,
        env_config: _AI21EnvConfig = AI21EnvConfig,
    ):
        import boto3

        self._session = (
            session.client(_RUNTIME_NAME) if session else boto3.client(_RUNTIME_NAME, region_name=env_config.aws_region)
        )
        self.completion = BedrockCompletion(self)

    def invoke_model(self, model_id: str, input_json: str) -> Dict[str, Any]:
        from botocore.exceptions import ClientError

        try:
            response = self._session.invoke_model(
                modelId=model_id,
                contentType="application/json",
                accept="application/json",
                body=input_json,
            )

            return json.loads(response.get("body").read())

        except ClientError as client_error:
            self._handle_client_error(client_error)
        except Exception as exception:
            log_error(f"Calling {model_id} failed with Exception: {exception}")
            raise exception

    def _handle_client_error(self, client_exception: "ClientError") -> None:
        error_response = client_exception.response
        error_message = error_response.get("Error", {}).get("Message", "")
        status_code = error_response.get("ResponseMetadata", {}).get("HTTPStatusCode", None)
        # As written in https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html

        if status_code == 403:
            raise AccessDenied(details=error_message)

        if status_code == 404:
            raise NotFound(details=error_message)

        if status_code == 408:
            raise APITimeoutError(details=error_message)

        if status_code == 424:
            error_message_template = re.compile(_ERROR_MSG_TEMPLATE)
            model_status_code = int(error_message_template.search(error_message).group(1))
            model_error_message = error_message_template.search(error_message).group(2)
            handle_non_success_response(model_status_code, model_error_message)

        handle_non_success_response(status_code, error_message)
