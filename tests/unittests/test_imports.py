# The following line should not be removed, as it is used to test the imports in runtime
# noinspection PyUnresolvedReferences
from ai21 import *  # noqa: F403
from ai21 import __all__


EXPECTED_ALL = [
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
    "AI21LaunchpadClient",
    "AsyncAI21LaunchpadClient",
]


def test_all_imports() -> None:
    assert sorted(EXPECTED_ALL) == sorted(__all__)
