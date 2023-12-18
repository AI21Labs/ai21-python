import logging

from ai21.ai21_env_config import AI21EnvConfig

logger = logging.getLogger("ai21")


def _basic_config() -> None:
    logging.basicConfig(
        format="[%(asctime)s - %(name)s - %(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def setup_logger() -> None:
    _basic_config()

    if AI21EnvConfig.log_level == "debug":
        logger.setLevel(logging.DEBUG)
    elif AI21EnvConfig.log_level == "info":
        logger.setLevel(logging.INFO)
