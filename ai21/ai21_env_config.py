from __future__ import annotations
import os
from dataclasses import dataclass
from typing import Optional

from ai21.constants import DEFAULT_API_VERSION, STUDIO_HOST


@dataclass(frozen=True)
class _AI21EnvConfig:
    api_key: Optional[str] = None
    api_version: str = DEFAULT_API_VERSION
    api_host: str = STUDIO_HOST
    timeout_sec: Optional[int] = None
    num_retries: Optional[int] = None
    aws_region: Optional[str] = None
    log_level: Optional[str] = None

    @classmethod
    def from_env(cls) -> _AI21EnvConfig:
        return cls(
            api_key=os.getenv("AI21_API_KEY"),
            api_version=os.getenv("AI21_API_VERSION", DEFAULT_API_VERSION),
            api_host=os.getenv("AI21_API_HOST", STUDIO_HOST),
            timeout_sec=os.getenv("AI21_TIMEOUT_SEC"),
            num_retries=os.getenv("AI21_NUM_RETRIES"),
            aws_region=os.getenv("AI21_AWS_REGION", "us-east-1"),
            log_level=os.getenv("AI21_LOG_LEVEL", "info"),
        )


AI21EnvConfig = _AI21EnvConfig.from_env()
