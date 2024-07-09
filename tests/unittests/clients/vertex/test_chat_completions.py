import json
from typing import Optional
from unittest.mock import Mock, patch, ANY

import httpx
import pytest

from ai21 import AI21VertexClient
from ai21.clients.vertex.ai21_vertex_client import DEFAULT_GCP_REGION, AsyncAI21VertexClient
from ai21.clients.vertex.gcp_authorization import GCPAuthorization
from ai21.models.chat import ChatMessage
from tests.unittests.commons import FAKE_CHAT_COMPLETION_RESPONSE_DICT, FAKE_AUTH_HEADERS

_TEST_REGION = "test-region"
_TEST_PROJECT = "test-project"
_FULL_GCP_URL = f"https://{_TEST_REGION}-aiplatform.googleapis.com/v1/projects/{_TEST_PROJECT}/locations/{_TEST_REGION}/publishers/ai21/models/jamba-instruct:rawPredict"


def test__vertex_client__when_no_region_provided__should_use_default_region():
    client = AI21VertexClient()
    assert client._region == DEFAULT_GCP_REGION


@pytest.mark.parametrize(
    ids=[
        "when_no_region__should_use_default_region",
        "with_region__should_use_given_region",
    ],
    argvalues=[(None,), (_TEST_REGION,)],
    argnames=["region"],
)
def test_client__base_url_with_region(region: Optional[str]) -> None:
    client = AI21VertexClient(region=region)

    if region is None:
        region = DEFAULT_GCP_REGION

    assert client._base_url == f"https://{region}-aiplatform.googleapis.com/v1"


def test__options_in_request(mock_httpx_client: Mock):
    message = ChatMessage(content="This is a test", role="user")

    mock_httpx_client.send.return_value = httpx.Response(
        status_code=200,
        content=json.dumps(FAKE_CHAT_COMPLETION_RESPONSE_DICT).encode("utf-8"),
    )

    with patch.object(GCPAuthorization, GCPAuthorization.get_access_token.__name__, return_value="fake-token"):
        client = AI21VertexClient(http_client=mock_httpx_client, project_id=_TEST_PROJECT, region=_TEST_REGION)
        client.chat.completions.create(model="jamba-instruct", messages=[message])

    mock_httpx_client.build_request.assert_called_once_with(
        method="POST",
        url=_FULL_GCP_URL,
        headers={
            "Content-Type": "application/json",
            "User-Agent": ANY,
            **FAKE_AUTH_HEADERS,
        },
        timeout=300,
        params={},
        data=json.dumps({"messages": [message.to_dict()]}).encode("utf-8"),
        files=None,
    )


@pytest.mark.asyncio
async def test__async_options_in_request(mock_httpx_async_client: Mock):
    message = ChatMessage(content="This is a test", role="user")

    mock_httpx_async_client.send.return_value = httpx.Response(
        status_code=200,
        content=json.dumps(FAKE_CHAT_COMPLETION_RESPONSE_DICT).encode("utf-8"),
    )

    with patch.object(GCPAuthorization, GCPAuthorization.get_access_token.__name__, return_value="fake-token"):
        client = AsyncAI21VertexClient(
            http_client=mock_httpx_async_client, project_id=_TEST_PROJECT, region=_TEST_REGION
        )
        await client.chat.completions.create(model="jamba-instruct", messages=[message])

    mock_httpx_async_client.build_request.assert_called_once_with(
        method="POST",
        url=_FULL_GCP_URL,
        headers={
            "Content-Type": "application/json",
            "User-Agent": ANY,
            **FAKE_AUTH_HEADERS,
        },
        timeout=300,
        params={},
        data=json.dumps({"messages": [message.to_dict()]}).encode("utf-8"),
        files=None,
    )


def test__vertex_client__when_passing_access_token__should_use_the_access_token(mock_httpx_client: Mock):
    message = ChatMessage(content="This is a test", role="user")
    custom_access_token = "custom-access-token"

    mock_httpx_client.send.return_value = httpx.Response(
        status_code=200,
        content=json.dumps(FAKE_CHAT_COMPLETION_RESPONSE_DICT).encode("utf-8"),
    )

    with patch.object(GCPAuthorization, GCPAuthorization.get_access_token.__name__, return_value="fake-token"):
        client = AI21VertexClient(
            http_client=mock_httpx_client,
            project_id=_TEST_PROJECT,
            region=_TEST_REGION,
            access_token=custom_access_token,
        )
        client.chat.completions.create(model="jamba-instruct", messages=[message])

    mock_httpx_client.build_request.assert_called_once_with(
        method="POST",
        url=_FULL_GCP_URL,
        headers={
            "Content-Type": "application/json",
            "User-Agent": ANY,
            **{"Authorization": f"Bearer {custom_access_token}"},
        },
        timeout=300,
        params={},
        data=json.dumps({"messages": [message.to_dict()]}).encode("utf-8"),
        files=None,
    )


@pytest.mark.asyncio
async def test__async_vertex_client__when_passing_access_token__should_use_the_access_token(
    mock_httpx_async_client: Mock,
):
    message = ChatMessage(content="This is a test", role="user")
    custom_access_token = "custom-access-token"

    mock_httpx_async_client.send.return_value = httpx.Response(
        status_code=200,
        content=json.dumps(FAKE_CHAT_COMPLETION_RESPONSE_DICT).encode("utf-8"),
    )

    with patch.object(GCPAuthorization, GCPAuthorization.get_access_token.__name__, return_value="fake-token"):
        client = AsyncAI21VertexClient(
            http_client=mock_httpx_async_client,
            project_id=_TEST_PROJECT,
            region=_TEST_REGION,
            access_token=custom_access_token,
        )
        await client.chat.completions.create(model="jamba-instruct", messages=[message])

    mock_httpx_async_client.build_request.assert_called_once_with(
        method="POST",
        url=_FULL_GCP_URL,
        headers={
            "Content-Type": "application/json",
            "User-Agent": ANY,
            **{"Authorization": f"Bearer {custom_access_token}"},
        },
        timeout=300,
        params={},
        data=json.dumps({"messages": [message.to_dict()]}).encode("utf-8"),
        files=None,
    )
