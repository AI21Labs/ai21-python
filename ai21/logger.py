import logging
import os
import re

from ai21.ai21_env_config import AI21EnvConfig

_verbose = False

logger = logging.getLogger("ai21")
httpx_logger = logging.getLogger("httpx")


class CensorSecretsFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        # Get original log message
        message = super().format(record)

        if not get_verbose():
            return self._censor_secrets(message)

        return message

    def _censor_secrets(self, message: str) -> str:
        # Regular expression to find the Authorization key and its value
        pattern = r"('Authorization':\s*'[^']*'|'api-key':\s*'[^']*'|'X-Amz-Security-Token':\s*'[^']*')"

        def replacement(match):
            return match.group(0).split(":")[0] + ": '**************'"

        # Substitute the Authorization value with **************
        return re.sub(pattern, replacement, message)


def set_verbose(value: bool) -> None:
    """
    Use this function if you want to log additional, more sensitive data like - secrets and environment variables.
    Log level will be set to DEBUG if verbose is set to True.
    """
    global _verbose
    _verbose = value

    set_debug(_verbose)

    AI21EnvConfig.log(with_secrets=value)


def set_debug(value: bool) -> None:
    """
    Additional way to set log level to DEBUG.
    """
    if value:
        os.environ["AI21_LOG_LEVEL"] = "debug"
    else:
        os.environ["AI21_LOG_LEVEL"] = "info"

    setup_logger()


def get_verbose() -> bool:
    global _verbose
    return _verbose


def _basic_config() -> None:
    logging.basicConfig(
        format="[%(asctime)s - %(name)s - %(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def setup_logger() -> None:
    _basic_config()
    # Set the root handler with the censor formatter
    logger.root.handlers[0].setFormatter(CensorSecretsFormatter())

    if AI21EnvConfig.log_level.lower() == "debug":
        logger.setLevel(logging.DEBUG)
        httpx_logger.setLevel(logging.DEBUG)
    elif AI21EnvConfig.log_level.lower() == "info":
        logger.setLevel(logging.INFO)
