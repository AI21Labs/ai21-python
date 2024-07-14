from unittest.mock import Mock, patch

import google.auth.exceptions
import pytest
from google.auth.transport.requests import Request

from ai21.clients.vertex.gcp_authorization import GCPAuthorization
from ai21.errors import CredentialsError

_TEST_PROJECT_ID = "test-project"


@patch("google.auth.default")
@patch.object(GCPAuthorization, GCPAuthorization._get_gcp_request.__name__)
def test__get_gcp_credentials_and_project_id__when_project_id_not_found__should_raise_error(
    mock_gcp_request: Mock,
    mock_default: Mock,
    mock_gcp_credentials: Mock,
):
    mock_default.return_value = (mock_gcp_credentials, None)
    mock_gcp_request.return_value = Mock(spec=Request)

    auth = GCPAuthorization()

    with pytest.raises(ValueError):
        _, _ = auth.get_gcp_credentials_and_project_id(project_id=None)


@patch("google.auth.default")
@patch.object(GCPAuthorization, GCPAuthorization._get_gcp_request.__name__)
def test__get_gcp_credentials_and_project_id__when_project_id_found__should_set_auth(
    mock_gcp_request: Mock,
    mock_default: Mock,
    mock_gcp_credentials: Mock,
):
    mock_default.return_value = (mock_gcp_credentials, _TEST_PROJECT_ID)
    mock_gcp_request.return_value = Mock(spec=Request)

    auth = GCPAuthorization()
    credentials, project_id = auth.get_gcp_credentials_and_project_id(project_id=_TEST_PROJECT_ID)

    assert credentials == mock_gcp_credentials
    assert project_id == _TEST_PROJECT_ID


@patch("google.auth.default")
@patch.object(GCPAuthorization, GCPAuthorization._get_gcp_request.__name__)
def test__get_gcp_credentials_and_project_id__project_id_mismatch__should_raise_error(
    mock_gcp_request: Mock,
    mock_default: Mock,
    mock_gcp_credentials: Mock,
):
    mock_default.return_value = (mock_gcp_credentials, "another-project")
    mock_gcp_request.return_value = Mock(spec=Request)

    auth = GCPAuthorization()

    with pytest.raises(ValueError, match="Mismatch between credentials project id and 'project_id'"):
        _, _ = auth.get_gcp_credentials_and_project_id(project_id=_TEST_PROJECT_ID)


@patch.object(GCPAuthorization, GCPAuthorization._get_gcp_request.__name__)
def test__refresh_auth(
    mock_get_gcp_request: Mock,
    mock_gcp_request: Mock,
    mock_gcp_credentials: Mock,
):
    mock_get_gcp_request.return_value = mock_gcp_request
    auth = GCPAuthorization()
    auth.refresh_auth(credentials=mock_gcp_credentials)

    mock_gcp_credentials.refresh.assert_called_once_with(mock_gcp_request)


@patch("google.auth.default")
def test__get_gcp_credentials_and_project_id__should_return_credentials_and_project_id(
    mock_default: Mock,
    mock_gcp_credentials: Mock,
):
    mock_default.return_value = (mock_gcp_credentials, _TEST_PROJECT_ID)
    mock_gcp_credentials.token = "test-token"

    auth = GCPAuthorization()
    credentials, project_id = auth.get_gcp_credentials_and_project_id(project_id=_TEST_PROJECT_ID)

    assert credentials == mock_gcp_credentials
    assert project_id == _TEST_PROJECT_ID


def test__get_gcp_credentials_and_project_id__with_no_credentials__should_raise_error():
    auth = GCPAuthorization()
    auth.get_gcp_credentials_and_project_id = Mock(side_effect=ValueError("Could not get credentials for GCP project"))

    with pytest.raises(ValueError, match="Could not get credentials for GCP project"):
        auth.get_gcp_credentials_and_project_id(project_id=None)


@patch("google.auth.default")
@patch.object(GCPAuthorization, GCPAuthorization._get_gcp_request.__name__)
def test__get_gcp_credentials_and_project_id__with_default_credentials_error__should_raise_custom_credentials_error(
    mock_gcp_request: Mock,
    mock_default: Mock,
):
    mock_default.side_effect = google.auth.exceptions.DefaultCredentialsError(
        "Could not get project_id for GCP project"
    )
    auth = GCPAuthorization()

    with pytest.raises(CredentialsError, match="Could not get project_id for GCP project"):
        auth.get_gcp_credentials_and_project_id(project_id=None)
