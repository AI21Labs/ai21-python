from __future__ import annotations

from typing import Optional, Tuple

import google.auth
from google.auth.credentials import Credentials
from google.auth.transport.requests import Request
from google.auth.exceptions import DefaultCredentialsError

from ai21.errors import CredentialsError


class GCPAuthorization:
    def get_gcp_credentials(
        self,
        project_id: Optional[str] = None,
    ) -> Tuple[Credentials, str]:
        try:
            credentials, loaded_project_id = google.auth.default(
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
        except DefaultCredentialsError as e:
            raise CredentialsError(provider_name="GCP", error_message=str(e))

        if project_id is not None and project_id != loaded_project_id:
            raise ValueError("Mismatch between credentials project id and 'project_id'")

        project_id = project_id or loaded_project_id

        if project_id is None:
            raise ValueError("Could not get project_id for GCP project")

        if not isinstance(project_id, str):
            raise ValueError(f"Variable project_id must be a string, got {type(project_id)} instead")

        return credentials, project_id

    def _get_gcp_request(self) -> Request:
        return Request()

    def refresh_auth(self, credentials: Credentials) -> None:
        request = self._get_gcp_request()
        credentials.refresh(request)
