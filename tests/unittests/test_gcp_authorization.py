from typing import Optional

import pytest
from unittest.mock import Mock, patch
from google.auth.credentials import Credentials
from google.auth.exceptions import RefreshError

from ai21.clients.vertex.gcp_authorization import GCPAuthorization
from google.auth.transport.requests import Request

_TEST_PROJECT_ID = "test-project"


@pytest.mark.parametrize(
    ids=[
        "when_project_id_not_found__should_raise_error",
        "when_project_id_found__should_set_auth",
    ],
    argvalues=[(None,), (_TEST_PROJECT_ID,)],
    argnames=["project_id"],
)
@patch("google.auth.default")
@patch.object(GCPAuthorization, GCPAuthorization._get_gcp_request.__name__)
def test__gcp_authorization_set_auth(
    mock_gcp_request: Mock,
    mock_default: Mock,
    mock_gcp_credentials: Mock,
    project_id: Optional[str],
):
    mock_default.return_value = (mock_gcp_credentials, project_id)
    mock_gcp_request.return_value = Mock(spec=Request)

    auth = GCPAuthorization(project_id=project_id)

    if project_id is None:
        with pytest.raises(ValueError):
            auth._set_auth()
    else:
        auth._set_auth()
        assert auth._credentials == mock_gcp_credentials
        assert auth.project_id == _TEST_PROJECT_ID


@patch("google.auth.default")
@patch.object(GCPAuthorization, GCPAuthorization._get_gcp_request.__name__)
def test__gcp_authorization_set_auth__project_id_mismatch__should_raise_error(
    mock_gcp_request: Mock,
    mock_default: Mock,
    mock_gcp_credentials: Mock,
):
    mock_default.return_value = (mock_gcp_credentials, "another-project")
    mock_gcp_request.return_value = Mock(spec=Request)

    auth = GCPAuthorization(project_id=_TEST_PROJECT_ID)

    with pytest.raises(ValueError):
        auth._set_auth()


@patch.object(GCPAuthorization, GCPAuthorization._get_gcp_request.__name__)
def test__gcp_authorization_refresh_auth(
    mock_gcp_request: Mock,
    mock_gcp_credentials: Mock,
):
    auth = GCPAuthorization(credentials=mock_gcp_credentials)
    auth._refresh_auth(mock_gcp_request)

    mock_gcp_credentials.refresh.assert_called_once_with(mock_gcp_request)


@patch("google.auth.default")
def test__gcp_authorization_get_access_token_success(
    mock_default: Mock,
    mock_gcp_credentials: Mock,
):
    mock_default.return_value = (mock_gcp_credentials, _TEST_PROJECT_ID)
    mock_gcp_credentials.token = "test-token"

    auth = GCPAuthorization()
    token = auth.get_access_token()

    assert token == "test-token"
    mock_gcp_credentials.refresh.assert_called_once()


def test__gcp_authorization_get_access_token_no_credentials__should_raise_error():
    auth = GCPAuthorization()
    auth._set_auth = Mock(side_effect=ValueError("Could not get credentials for GCP project"))

    with pytest.raises(ValueError, match="Could not get credentials for GCP project"):
        auth.get_access_token()


def test__gcp_authorization_get_access_token_no_token__should_raise_error(mock_gcp_credentials: Mock):
    mock_gcp_credentials.token = None
    auth = GCPAuthorization(credentials=mock_gcp_credentials)

    with pytest.raises(RuntimeError, match="Could not get access token for GCP project"):
        auth.get_access_token()


@patch("google.auth.default")
def test__gcp_authorization_project_id_property(mock_default: Mock):
    mock_default.return_value = (Mock(spec=Credentials), _TEST_PROJECT_ID)

    auth = GCPAuthorization()
    assert auth.project_id == _TEST_PROJECT_ID


def test__gcp_authorization_project_id_property_preset():
    auth = GCPAuthorization(project_id="preset-project")
    assert auth.project_id == "preset-project"


@patch("google.auth.default")
def test__gcp_authorization_get_access_token_refresh_error__should_raise_error(
    mock_default: Mock,
    mock_gcp_credentials: Mock,
):
    mock_default.return_value = (mock_gcp_credentials, _TEST_PROJECT_ID)
    mock_gcp_credentials.refresh.side_effect = RefreshError("Token refresh failed")

    auth = GCPAuthorization()
    with pytest.raises(RefreshError, match="Token refresh failed"):
        auth.get_access_token()
