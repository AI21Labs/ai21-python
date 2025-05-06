import boto3
import httpx
import pytest

from google.auth.credentials import Credentials
from google.auth.transport.requests import Request

from ai21.clients.common.auth.gcp_authorization import GCPAuthorization
from ai21.clients.vertex.ai21_vertex_client import AI21VertexClient


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


@pytest.fixture
def mock_boto_session(mocker) -> boto3.Session:
    boto_mocker = mocker.Mock(spec=boto3.Session)
    boto_mocker.region_name = "us-east-1"
    return boto_mocker


@pytest.fixture
def mock_gcp_credentials(mocker) -> Credentials:
    return mocker.Mock(spec=Credentials)


@pytest.fixture
def mock_gcp_request(mocker) -> Request:
    return mocker.Mock(spec=Request)


@pytest.fixture
def mock_ai21_vertex_client(mocker) -> AI21VertexClient:
    ai21_vertex_client_mock = mocker.Mock(spec=AI21VertexClient)
    ai21_vertex_client_mock._gcp_auth = mocker.Mock(spec=GCPAuthorization)
    return ai21_vertex_client_mock
