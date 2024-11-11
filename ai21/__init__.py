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
from ai21.version import VERSION

__version__ = VERSION
setup_logger()


def _import_bedrock_client():
    from ai21.clients.bedrock.ai21_bedrock_client import AI21BedrockClient

    return AI21BedrockClient


def _import_bedrock_model_id():
    from ai21.clients.bedrock.bedrock_model_id import BedrockModelID

    return BedrockModelID


def _import_async_bedrock_client():
    from ai21.clients.bedrock.ai21_bedrock_client import AsyncAI21BedrockClient

    return AsyncAI21BedrockClient


def _import_vertex_client():
    from ai21.clients.vertex.ai21_vertex_client import AI21VertexClient

    return AI21VertexClient


def _import_async_vertex_client():
    from ai21.clients.vertex.ai21_vertex_client import AsyncAI21VertexClient

    return AsyncAI21VertexClient


def __getattr__(name: str) -> Any:
    try:
        if name == "AI21BedrockClient":
            return _import_bedrock_client()

        if name == "BedrockModelID":
            return _import_bedrock_model_id()

        if name == "AsyncAI21BedrockClient":
            return _import_async_bedrock_client()

        if name == "AI21VertexClient":
            return _import_vertex_client()

        if name == "AsyncAI21VertexClient":
            return _import_async_vertex_client()
    except ImportError as e:
        raise ImportError('Please install "ai21[AWS]" for Bedrock, or "ai21[Vertex]" for Vertex') from e


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
    "BedrockModelID",
    "AI21AzureClient",
    "AsyncAI21AzureClient",
    "AsyncAI21BedrockClient",
    "AI21VertexClient",
    "AsyncAI21VertexClient",
]
