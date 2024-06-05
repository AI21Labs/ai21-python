import pytest
import httpx


@pytest.fixture
def dummy_api_host() -> str:
    return "http://test_host"


@pytest.fixture
def mock_httpx_client(mocker) -> httpx.Client:
    return mocker.Mock(spec=httpx.Client)


@pytest.fixture
def mock_httpx_async_client(mocker) -> httpx.AsyncClient:
    return mocker.AsyncMock(spec=httpx.AsyncClient)


@pytest.fixture
def mock_httpx_response(mocker) -> httpx.Response:
    return mocker.Mock(spec=httpx.Response)
