from typing import Any

from ai21.ai21_env_config import AI21EnvConfig
from ai21.clients.azure.ai21_azure_client import AI21AzureClient, AsyncAI21AzureClient
from ai21.clients.studio.ai21_client import AI21Client
from ai21.clients.studio.async_ai21_client import AsyncAI21Client

from ai21.errors import (
    AI21APIError,
    APITimeoutError,
    MissingApiKeyError,
    ModelPackageDoesntExistError,
    AI21Error,
    TooManyRequestsError,
)
from ai21.logger import setup_logger
from ai21.services.sagemaker import SageMaker
from ai21.version import VERSION

__version__ = VERSION
setup_logger()


def _import_bedrock_client():
    from ai21.clients.bedrock.ai21_bedrock_client import AI21BedrockClient

    return AI21BedrockClient


def _import_sagemaker_client():
    from ai21.clients.sagemaker.ai21_sagemaker_client import AI21SageMakerClient

    return AI21SageMakerClient


def _import_bedrock_model_id():
    from ai21.clients.bedrock.bedrock_model_id import BedrockModelID

    return BedrockModelID


def _import_async_bedrock_client():
    from ai21.clients.bedrock.ai21_bedrock_client import AsyncAI21BedrockClient

    return AsyncAI21BedrockClient


def _import_async_sagemaker_client():
    from ai21.clients.sagemaker.ai21_sagemaker_client import AsyncAI21SageMakerClient

    return AsyncAI21SageMakerClient


def __getattr__(name: str) -> Any:
    try:
        if name == "AI21BedrockClient":
            return _import_bedrock_client()

        if name == "AI21SageMakerClient":
            return _import_sagemaker_client()

        if name == "BedrockModelID":
            return _import_bedrock_model_id()

        if name == "AsyncAI21BedrockClient":
            return _import_async_bedrock_client()

        if name == "AsyncAI21SageMakerClient":
            return _import_async_sagemaker_client()
    except ImportError as e:
        raise ImportError(f'Please install "ai21[AWS]" in order to use {name}') from e


__all__ = [
    "AI21EnvConfig",
    "AI21Client",
    "AsyncAI21Client",
    "AI21APIError",
    "APITimeoutError",
    "AI21Error",
    "MissingApiKeyError",
    "ModelPackageDoesntExistError",
    "TooManyRequestsError",
    "AI21BedrockClient",
    "AI21SageMakerClient",
    "BedrockModelID",
    "SageMaker",
    "AI21AzureClient",
    "AsyncAI21AzureClient",
    "AsyncAI21BedrockClient",
    "AsyncAI21SageMakerClient",
]
