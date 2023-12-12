from .version import VERSION
from .clients import AI21Client, AI21BedrockClient, AI21SageMakerClient

__version__ = VERSION

__all__ = ["AI21Client", "AI21BedrockClient", "AI21SageMakerClient", "BedrockModelID"]


class BedrockModelID:
    J2_MID_V1 = "ai21.j2-mid-v1"
    J2_ULTRA_V1 = "ai21.j2-ultra-v1"
