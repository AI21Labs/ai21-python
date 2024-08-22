from __future__ import annotations

from typing import Optional, Dict, Any

import httpx
from google.auth.credentials import Credentials as GCPCredentials

from ai21.clients.studio.resources.studio_chat import StudioChat, AsyncStudioChat
from ai21.clients.vertex.gcp_authorization import GCPAuthorization
from ai21.http_client.async_http_client import AsyncAI21HTTPClient
from ai21.http_client.http_client import AI21HTTPClient
from ai21.models.request_options import RequestOptions

_DEFAULT_GCP_REGION = "us-central1"
_VERTEX_BASE_URL_FORMAT = "https://{region}-aiplatform.googleapis.com/v1"
_VERTEX_PATH_FORMAT = "/projects/{project_id}/locations/{region}/publishers/ai21/models/{model}:{endpoint}"


class BaseAI21VertexClient:
    def __init__(
        self,
        region: Optional[str] = None,
        project_id: Optional[str] = None,
        access_token: Optional[str] = None,
        credentials: Optional[GCPCredentials] = None,
    ):
        if access_token is not None and project_id is None:
            raise ValueError("Field project_id is required when setting access_token")
        self._region = region or _DEFAULT_GCP_REGION
        self._access_token = access_token
        self._project_id = project_id
        self._credentials = credentials
        self._gcp_auth = GCPAuthorization()

    def _get_base_url(self) -> str:
        return _VERTEX_BASE_URL_FORMAT.format(region=self._region)

    def _get_access_token(self) -> str:
        if self._access_token is not None:
            return self._access_token

        if self._credentials is None:
            self._credentials, self._project_id = self._gcp_auth.get_gcp_credentials(
                project_id=self._project_id,
            )

        if self._credentials is None:
            raise ValueError("Could not get credentials for GCP project")

        self._gcp_auth.refresh_auth(self._credentials)

        if self._credentials.token is None:
            raise RuntimeError(f"Could not get access token for GCP project {self._project_id}")

        return self._credentials.token

    def _build_path(
        self,
        project_id: str,
        region: str,
        model: str,
        endpoint: str,
    ) -> str:
        return _VERTEX_PATH_FORMAT.format(
            project_id=project_id,
            region=region,
            model=model,
            endpoint=endpoint,
        )

    def _get_authorization_header(self) -> Dict[str, Any]:
        access_token = self._get_access_token()
        return {"Authorization": f"Bearer {access_token}"}


class AI21VertexClient(BaseAI21VertexClient, AI21HTTPClient):
    def __init__(
        self,
        region: Optional[str] = None,
        project_id: Optional[str] = None,
        base_url: Optional[str] = None,
        access_token: Optional[str] = None,
        credentials: Optional[GCPCredentials] = None,
        headers: Dict[str, str] | None = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        http_client: Optional[httpx.Client] = None,
    ):
        BaseAI21VertexClient.__init__(
            self,
            region=region,
            project_id=project_id,
            access_token=access_token,
            credentials=credentials,
        )

        if base_url is None:
            base_url = self._get_base_url()

        AI21HTTPClient.__init__(
            self,
            base_url=base_url,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            headers=headers,
            client=http_client,
            requires_api_key=False,
        )

        self.chat = StudioChat(self)
        # Override the chat.create method to match the completions endpoint,
        # so it wouldn't get to the old J2 completion endpoint
        self.chat.create = self.chat.completions.create

    def _build_request(self, options: RequestOptions) -> httpx.Request:
        options = self._prepare_options(options)

        return super()._build_request(options)

    def _prepare_options(self, options: RequestOptions) -> RequestOptions:
        body = options.body

        model = body.pop("model")
        stream = body.pop("stream", False)
        endpoint = "streamRawPredict" if stream else "rawPredict"
        headers = self._prepare_headers()
        path = self._build_path(
            project_id=self._project_id,
            region=self._region,
            model=model,
            endpoint=endpoint,
        )

        return options.replace(
            body=body,
            path=path,
            headers=headers,
        )

    def _prepare_headers(self) -> Dict[str, Any]:
        return self._get_authorization_header()


class AsyncAI21VertexClient(BaseAI21VertexClient, AsyncAI21HTTPClient):
    def __init__(
        self,
        region: Optional[str] = None,
        project_id: Optional[str] = None,
        base_url: Optional[str] = None,
        access_token: Optional[str] = None,
        credentials: Optional[GCPCredentials] = None,
        headers: Dict[str, str] | None = None,
        timeout_sec: Optional[float] = None,
        num_retries: Optional[int] = None,
        http_client: Optional[httpx.AsyncClient] = None,
    ):
        BaseAI21VertexClient.__init__(
            self,
            region=region,
            project_id=project_id,
            access_token=access_token,
            credentials=credentials,
        )

        if base_url is None:
            base_url = self._get_base_url()

        AsyncAI21HTTPClient.__init__(
            self,
            base_url=base_url,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            headers=headers,
            client=http_client,
            requires_api_key=False,
        )

        self.chat = AsyncStudioChat(self)
        # Override the chat.create method to match the completions endpoint,
        # so it wouldn't get to the old J2 completion endpoint
        self.chat.create = self.chat.completions.create

    def _build_request(self, options: RequestOptions) -> httpx.Request:
        options = self._prepare_options(options)

        return super()._build_request(options)

    def _prepare_options(self, options: RequestOptions) -> RequestOptions:
        body = options.body

        model = body.pop("model")
        stream = body.pop("stream", False)
        endpoint = "streamRawPredict" if stream else "rawPredict"
        headers = self._prepare_headers()
        path = self._build_path(
            project_id=self._project_id,
            region=self._region,
            model=model,
            endpoint=endpoint,
        )

        return options.replace(
            body=body,
            path=path,
            headers=headers,
        )

    def _prepare_headers(self) -> Dict[str, Any]:
        return self._get_authorization_header()
