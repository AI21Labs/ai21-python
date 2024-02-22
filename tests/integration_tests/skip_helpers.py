import os


def should_skip_bedrock_integration_tests() -> bool:
    return os.getenv("AWS_ACCESS_KEY_ID") is None or os.getenv("AWS_SECRET_ACCESS_KEY") is None


def should_skip_studio_integration_tests() -> bool:
    return os.getenv("AI21_API_KEY") is None
