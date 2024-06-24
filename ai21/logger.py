import os
import logging

from ai21.ai21_env_config import AI21EnvConfig

_verbose = False

logger = logging.getLogger("ai21")
httpx_logger = logging.getLogger("httpx")


def set_verbose(value: bool) -> None:
    """ "
    Use this function if you want to log additional, more sensitive data like - secrets and environment variables.
    Log level will be set to DEBUG if verbose is set to True.
    """
    global _verbose
    _verbose = value

    set_debug(_verbose)


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


def log_verbose(text: str) -> None:
    if get_verbose():
        logger.info(text)


def setup_logger() -> None:
    _basic_config()

    if AI21EnvConfig.log_level.lower() == "debug":
        logger.setLevel(logging.DEBUG)
        httpx_logger.setLevel(logging.DEBUG)
    elif AI21EnvConfig.log_level.lower() == "info":
        logger.setLevel(logging.INFO)
        httpx_logger.setLevel(logging.INFO)
