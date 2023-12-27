from typing import Any

from ai21.clients.studio.ai21_client import AI21Client
from ai21.errors import (
    AI21APIError,
    APITimeoutError,
    MissingApiKeyError,
    ModelPackageDoesntExistError,
    AI21Error,
    TooManyRequestsError,
)
from ai21.logger import setup_logger
from ai21.resources.responses.answer_response import AnswerResponse
from ai21.resources.responses.chat_response import ChatResponse
from ai21.resources.responses.completion_response import CompletionsResponse
from ai21.resources.responses.custom_model_response import CustomBaseModelResponse
from ai21.resources.responses.dataset_response import DatasetResponse
from ai21.resources.responses.embed_response import EmbedResponse
from ai21.resources.responses.file_response import FileResponse
from ai21.resources.responses.gec_response import GECResponse
from ai21.resources.responses.improvement_response import ImprovementsResponse
from ai21.resources.responses.library_answer_response import LibraryAnswerResponse
from ai21.resources.responses.library_search_response import LibrarySearchResponse
from ai21.resources.responses.paraphrase_response import ParaphraseResponse
from ai21.resources.responses.segmentation_response import SegmentationResponse
from ai21.resources.responses.summarize_by_segment_response import SummarizeBySegmentResponse
from ai21.resources.responses.summarize_response import SummarizeResponse
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


def __getattr__(name: str) -> Any:
    try:
        if name == "AI21BedrockClient":
            return _import_bedrock_client()

        if name == "AI21SageMakerClient":
            return _import_sagemaker_client()

        if name == "BedrockModelID":
            return _import_bedrock_model_id()
    except ImportError as e:
        raise ImportError(f'Please install "ai21[AWS]" in order to use {name}') from e


__all__ = [
    "AI21Client",
    "AI21APIError",
    "APITimeoutError",
    "AI21Error",
    "MissingApiKeyError",
    "ModelPackageDoesntExistError",
    "TooManyRequestsError",
    "AI21BedrockClient",
    "AI21SageMakerClient",
    "BedrockModelID",
    "AnswerResponse",
    "ChatResponse",
    "CompletionsResponse",
    "CustomBaseModelResponse",
    "DatasetResponse",
    "EmbedResponse",
    "FileResponse",
    "GECResponse",
    "ImprovementsResponse",
    "LibraryAnswerResponse",
    "LibrarySearchResponse",
    "ParaphraseResponse",
    "SageMaker",
    "SegmentationResponse",
    "SummarizeBySegmentResponse",
    "SummarizeResponse",
]
