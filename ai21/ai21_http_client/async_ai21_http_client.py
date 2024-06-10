from typing import Optional, Dict, Any, BinaryIO

import httpx

from ai21.http_client.async_http_client import AsyncHttpClient
from ai21.ai21_http_client.base_ai21_http_client import BaseAI21HTTPClient


class AsyncAI21HTTPClient(BaseAI21HTTPClient):
    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        requires_api_key: bool = True,
        base_url: Optional[str] = None,
        api_version: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout_sec: Optional[int] = None,
        num_retries: Optional[int] = None,
        via: Optional[str] = None,
        http_client: Optional[AsyncHttpClient] = None,
    ):
        super().__init__(
            api_key=api_key,
            requires_api_key=requires_api_key,
            base_url=base_url,
            api_version=api_version,
            headers=headers,
            timeout_sec=timeout_sec,
            num_retries=num_retries,
            via=via,
        )

        headers = self._build_headers(passed_headers=headers)
        self._http_client = self._init_http_client(http_client=http_client, headers=headers)

    def _init_http_client(self, http_client: Optional[AsyncHttpClient], headers: Dict[str, Any]) -> AsyncHttpClient:
        if http_client is None:
            return AsyncHttpClient(
                timeout_sec=self._timeout_sec,
                num_retries=self._num_retries,
                headers=headers,
            )

        http_client.add_headers(headers)

        return http_client

    async def execute_http_request(
        self,
        method: str,
        path: str,
        params: Optional[Dict] = None,
        body: Optional[Dict] = None,
        stream: bool = False,
        files: Optional[Dict[str, BinaryIO]] = None,
    ) -> httpx.Response:
        return await self._http_client.execute_http_request(
            method=method,
            url=f"{self._base_url}{path}",
            params=params or {},
            files=files,
            stream=stream,
            body=body or {},
        )
