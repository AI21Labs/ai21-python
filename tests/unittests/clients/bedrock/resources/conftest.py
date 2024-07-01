from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from ai21.http_client.async_http_client import AsyncHttpClient
from ai21.http_client.http_client import HttpClient


@pytest.fixture
def mock_http_client(mocker: MockerFixture) -> Mock:
    return mocker.MagicMock(spec=HttpClient)


@pytest.fixture
def mock_async_http_client(mocker: MockerFixture) -> Mock:
    return mocker.MagicMock(spec=AsyncHttpClient)
