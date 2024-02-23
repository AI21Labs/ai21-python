from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from ai21.clients.bedrock.bedrock_session import BedrockSession


@pytest.fixture
def mock_bedrock_session(mocker: MockerFixture) -> Mock:
    return mocker.MagicMock(spec=BedrockSession)
