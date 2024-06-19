from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from ai21.clients.aws_http_client.aws_http_client import AWSHttpClient, AsyncAWSHttpClient


@pytest.fixture
def mock_aws_http_client(mocker: MockerFixture) -> Mock:
    return mocker.MagicMock(spec=AWSHttpClient)


@pytest.fixture
def mock_async_aws_http_client(mocker: MockerFixture) -> Mock:
    return mocker.MagicMock(spec=AsyncAWSHttpClient)
