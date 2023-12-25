import pytest
import requests


@pytest.fixture
def dummy_api_host() -> str:
    return "http://test_host"


@pytest.fixture
def mock_requests_session(mocker) -> requests.Session:
    return mocker.Mock(spec=requests.Session)
