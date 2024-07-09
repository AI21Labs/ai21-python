from __future__ import annotations

from typing import Optional

import google.auth
from google.auth.credentials import Credentials
from google.auth.transport.requests import Request


class GCPAuthorization:
    def __init__(self, credentials: Optional[Credentials] = None, project_id: Optional[str] = None):
        self._credentials = credentials
        self._project_id = project_id

    def _set_auth(self):
        credentials, loaded_project_id = google.auth.default(
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

        if self._project_id is not None and self._project_id != loaded_project_id:
            raise ValueError("Mismatch between credentials project id and 'project_id'")

        if self._project_id is None:
            self._project_id = loaded_project_id

        if self._project_id is None:
            raise ValueError("Could not get project_id for GCP project")

        if not isinstance(self._project_id, str):
            raise ValueError(f"Variable project_id must be a string, got {type(self._project_id)} instead")

        self._credentials = credentials

    def _get_gcp_request(self) -> Request:
        return Request()

    def _refresh_auth(self, request: Request):
        self._credentials.refresh(request)

    def get_access_token(self) -> str:
        if self._credentials is None:
            self._set_auth()
        self._refresh_auth(self._get_gcp_request())

        if self._credentials is None:
            raise ValueError("Could not get credentials for GCP project")

        if self._credentials.token is None:
            raise RuntimeError(f"Could not get access token for GCP project {self._project_id}")

        return self._credentials.token

    @property
    def project_id(self) -> str:
        if self._project_id is None:
            self._set_auth()

        return self._project_id
