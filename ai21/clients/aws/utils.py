from typing import Optional

import boto3

from ai21.ai21_env_config import _AI21EnvConfig


def get_aws_region(
    env_config: _AI21EnvConfig,
    session: Optional[boto3.Session] = None,
    region: Optional[str] = None,
) -> str:
    if session is not None:
        return session.region_name

    return region or env_config.aws_region
