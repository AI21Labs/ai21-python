from dataclasses import dataclass
from typing import Any, Dict, Optional, BinaryIO

from typing_extensions import Self


@dataclass(frozen=True)
class RequestOptions:
    url: str
    body: Dict[str, Any]
    method: str
    headers: Dict[str, Any]
    timeout: float
    path: Optional[str] = None
    params: Optional[Dict[str, Any]] = None
    stream: bool = False
    files: Optional[Dict[str, BinaryIO]] = None

    def replace(
        self,
        url: Optional[str] = None,
        body: Optional[Dict[str, Any]] = None,
        method: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        params: Optional[Dict[str, Any]] = None,
        stream: Optional[bool] = None,
        path: Optional[str] = None,
        files: Optional[Dict[str, BinaryIO]] = None,
    ) -> Self:
        return RequestOptions(
            url=url or self.url,
            body=body or self.body,
            method=method or self.method,
            headers=headers or self.headers,
            timeout=timeout or self.timeout,
            params=params or self.params,
            stream=stream if stream is not None else self.stream,
            path=path or self.path,
            files=files or self.files,
        )
