from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Optional

from ai21.constants import DEFAULT_API_VERSION, STUDIO_HOST

# Constants for environment variable keys
_ENV_API_KEY = "AI21_API_KEY"
_ENV_API_VERSION = "AI21_API_VERSION"
_ENV_API_HOST = "AI21_API_HOST"
_ENV_TIMEOUT_SEC = "AI21_TIMEOUT_SEC"
_ENV_NUM_RETRIES = "AI21_NUM_RETRIES"
_ENV_AWS_REGION = "AI21_AWS_REGION"
_ENV_LOG_LEVEL = "AI21_LOG_LEVEL"

_logger = logging.getLogger(__name__)


@dataclass
class _AI21EnvConfig:
    _api_key: Optional[str] = None
    _api_version: str = DEFAULT_API_VERSION
    _api_host: str = STUDIO_HOST
    _timeout_sec: Optional[int] = None
    _num_retries: Optional[int] = None
    _aws_region: Optional[str] = None
    _log_level: Optional[str] = None

    @classmethod
    def from_env(cls) -> _AI21EnvConfig:
        return cls(
            _api_key=os.getenv(_ENV_API_KEY),
            _api_version=os.getenv(_ENV_API_VERSION, DEFAULT_API_VERSION),
            _api_host=os.getenv(_ENV_API_HOST, STUDIO_HOST),
            _timeout_sec=os.getenv(_ENV_TIMEOUT_SEC),
            _num_retries=os.getenv(_ENV_NUM_RETRIES),
            _aws_region=os.getenv(_ENV_AWS_REGION, "us-east-1"),
            _log_level=os.getenv(_ENV_LOG_LEVEL, "info"),
        )

    @property
    def api_key(self) -> str:
        self._api_key = os.getenv(_ENV_API_KEY, self._api_key)
        return self._api_key

    @property
    def api_version(self) -> str:
        self._api_version = os.getenv(_ENV_API_VERSION, self._api_version)
        return self._api_version

    @property
    def api_host(self) -> str:
        self._api_host = os.getenv(_ENV_API_HOST, self._api_host)
        return self._api_host

    @property
    def timeout_sec(self) -> Optional[int]:
        timeout_str = os.getenv(_ENV_TIMEOUT_SEC)

        if timeout_str is not None:
            self._timeout_sec = int(timeout_str)

        return self._timeout_sec

    @property
    def num_retries(self) -> Optional[int]:
        retries_str = os.getenv(_ENV_NUM_RETRIES)

        if retries_str is not None:
            self._num_retries = int(retries_str)

        return self._num_retries

    @property
    def aws_region(self) -> Optional[str]:
        self._aws_region = os.getenv(_ENV_AWS_REGION, self._aws_region)
        return self._aws_region

    @property
    def log_level(self) -> Optional[str]:
        self._log_level = os.getenv(_ENV_LOG_LEVEL, self._log_level)
        return self._log_level

    def log(self, with_secrets: bool = False) -> None:
        env_vars = {
            _ENV_API_VERSION: self.api_version,
            _ENV_API_HOST: self.api_host,
            _ENV_TIMEOUT_SEC: self.timeout_sec,
            _ENV_NUM_RETRIES: self.num_retries,
            _ENV_AWS_REGION: self.aws_region,
            _ENV_LOG_LEVEL: self.log_level,
        }

        if with_secrets:
            env_vars[_ENV_API_KEY] = self.api_key

        _logger.debug(f"AI21 environment configuration: {env_vars}")


AI21EnvConfig = _AI21EnvConfig.from_env()
