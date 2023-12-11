import logging

from ai21.ai21_env_config import AI21EnvConfig

logger = logging.getLogger("ai21")


def log_info(message):
    if AI21EnvConfig.log_level == "debug":
        print(message)
        logger.debug(message)
    elif AI21EnvConfig.log_level == "info":
        logger.info(message)


def log_error(message):
    logger.error(message)


def log_warning(message):
    logger.warning(message)
