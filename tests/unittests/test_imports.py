# The following line should not be removed, as it is used to test the imports in runtime
# noinspection PyUnresolvedReferences
from ai21 import *  # noqa: F403
from ai21 import __all__

EXPECTED_ALL = [
    "AI21APIError",
    "AI21AzureClient",
    "AI21BedrockClient",
    "AI21Client",
    "AI21EnvConfig",
    "AI21Error",
    "AI21SageMakerClient",
    "APITimeoutError",
    "AsyncAI21AzureClient",
    "AsyncAI21Client",
    "BedrockModelID",
    "MissingApiKeyError",
    "ModelPackageDoesntExistError",
    "SageMaker",
    "TooManyRequestsError",
    "AsyncAI21BedrockClient",
    "AsyncAI21SageMakerClient",
]


def test_all_imports() -> None:
    assert sorted(EXPECTED_ALL) == sorted(__all__)
