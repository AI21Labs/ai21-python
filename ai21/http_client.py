import json
from typing import Optional, Dict, Any, BinaryIO

import requests
from requests.adapters import HTTPAdapter, Retry, RetryError

from ai21.errors import (
    BadRequest,
    Unauthorized,
    UnprocessableEntity,
    TooManyRequestsError,
    AI21ServerError,
    ServiceUnavailable,
    AI21APIError,
)
from ai21.logger import logger

DEFAULT_TIMEOUT_SEC = 300
DEFAULT_NUM_RETRIES = 0
RETRY_BACK_OFF_FACTOR = 0.5
TIME_BETWEEN_RETRIES = 1000
RETRY_ERROR_CODES = (429, 500, 503)
RETRY_METHOD_WHITELIST = ["GET", "POST", "PUT"]


def handle_non_success_response(status_code: int, response_text: str):
    if status_code == 400:
        raise BadRequest(details=response_text)
    if status_code == 401:
        raise Unauthorized(details=response_text)
    if status_code == 422:
        raise UnprocessableEntity(details=response_text)
    if status_code == 429:
        raise TooManyRequestsError(details=response_text)
    if status_code == 500:
        raise AI21ServerError(details=response_text)
    if status_code == 503:
        raise ServiceUnavailable(details=response_text)
    raise AI21APIError(status_code, details=response_text)


def requests_retry_session(session, retries=0):
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=RETRY_BACK_OFF_FACTOR,
        status_forcelist=RETRY_ERROR_CODES,
        method_whitelist=frozenset(RETRY_METHOD_WHITELIST),
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


class HttpClient:
    def __init__(
        self,
        session: Optional[requests.Session] = None,
        timeout_sec: int = None,
        num_retries: int = None,
        headers: Dict = None,
    ):
        self._timeout_sec = timeout_sec or DEFAULT_TIMEOUT_SEC
        self._num_retries = num_retries or DEFAULT_NUM_RETRIES
        self._headers = headers or {}
        self._apply_retry_policy = self._num_retries > 0
        self._session = self._init_session(session)

    def execute_http_request(
        self,
        method: str,
        url: str,
        params: Optional[Dict] = None,
        files: Optional[Dict[str, BinaryIO]] = None,
    ):
        timeout = self._timeout_sec
        headers = self._headers
        data = json.dumps(params).encode()
        logger.info(f"Calling {method} {url} {headers} {data}")
        try:
            if method == "GET":
                response = self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    timeout=timeout,
                    params=params,
                )
            elif files is not None:
                if method != "POST":
                    raise ValueError(
                        f"execute_http_request supports only POST for files upload, but {method} was supplied instead"
                    )
                if "Content-Type" in headers:
                    headers.pop(
                        "Content-Type"
                    )  # multipart/form-data 'Content-Type' is being added when passing rb files and payload
                response = self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    data=params,
                    files=files,
                    timeout=timeout,
                )
            else:
                response = self._session.request(method=method, url=url, headers=headers, data=data, timeout=timeout)
        except ConnectionError as connection_error:
            logger.error(f"Calling {method} {url} failed with ConnectionError: {connection_error}")
            raise connection_error
        except RetryError as retry_error:
            logger.error(
                f"Calling {method} {url} failed with RetryError after {self._num_retries} attempts: {retry_error}"
            )
            raise retry_error
        except Exception as exception:
            logger.error(f"Calling {method} {url} failed with Exception: {exception}")
            raise exception

        if response.status_code != 200:
            logger.error(f"Calling {method} {url} failed with a non-200 response code: {response.status_code}")
            handle_non_success_response(response.status_code, response.text)

        return response.json()

    def _init_session(self, session: Optional[requests.Session]) -> requests.Session:
        if session is not None:
            return session

        return (
            requests_retry_session(requests.Session(), retries=self._num_retries)
            if self._apply_retry_policy
            else requests.Session()
        )

    def add_headers(self, headers: Dict[str, Any]) -> None:
        self._headers.update(headers)
