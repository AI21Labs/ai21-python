import json
from typing import Optional, Union
from unittest.mock import Mock, patch, ANY

import httpx
import pytest
from pytest_mock import MockerFixture

from ai21 import AI21EnvConfig
from ai21.clients.aws.aws_authorization import AWSAuthorization
from ai21.clients.bedrock.ai21_bedrock_client import AI21BedrockClient, AsyncAI21BedrockClient
from ai21.clients.bedrock.bedrock_model_id import BedrockModelID
from ai21.models.chat import ChatMessage

_FAKE_RESPONSE_DICT = {
    "id": "cmpl-392a6a33e5204aa7a2070be4d0ddbc0a",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Test",
            },
            "logprobs": None,
            "finishReason": "stop",
        }
    ],
    "usage": {"promptTokens": 1, "completionTokens": 1, "totalTokens": 2},
}
_FAKE_AUTH_HEADERS = {"Authorization": "Bearer fake-token"}
_FULL_BEDROCK_URL = "https://bedrock-runtime.us-east-1.amazonaws.com/model/ai21.jamba-instruct-v1:0/invoke"


@pytest.fixture()
def mock_httpx_client(mocker: MockerFixture):
    return mocker.Mock(spec=httpx.Client)


@pytest.fixture()
def mock_async_httpx_client(mocker: MockerFixture):
    return mocker.Mock(spec=httpx.AsyncClient)


@pytest.mark.parametrize(
    ids=[
        "when_no_region__should_use_default_region",
        "with_region__should_use_given_region",
    ],
    argvalues=[(None,), ("us-east-2",)],
    argnames=["region"],
)
def test_client__base_url_with_region(region: Optional[str]) -> None:
    client = AI21BedrockClient(region=region)

    if region is None:
        region = AI21EnvConfig.aws_region

    assert client._base_url == f"https://bedrock-runtime.{region}.amazonaws.com"


def test__options_in_request(mock_httpx_client: Mock):
    message = ChatMessage(content="This is a test", role="user")

    mock_httpx_client.send.return_value = httpx.Response(
        status_code=200,
        content=json.dumps(_FAKE_RESPONSE_DICT).encode("utf-8"),
    )

    with patch.object(AWSAuthorization, AWSAuthorization.get_auth_headers.__name__, return_value=_FAKE_AUTH_HEADERS):
        client = AI21BedrockClient(http_client=mock_httpx_client)
        client.chat.completions.create(model=BedrockModelID.JAMBA_INSTRUCT_V1, messages=[message])

    mock_httpx_client.build_request.assert_called_once_with(
        method="POST",
        url=_FULL_BEDROCK_URL,
        headers={
            "Content-Type": "application/json",
            "User-Agent": ANY,
            **_FAKE_AUTH_HEADERS,
        },
        timeout=300,
        params={},
        data=json.dumps({"messages": [message.to_dict()]}).encode("utf-8"),
        files=None,
    )


@pytest.mark.asyncio
async def test__options_in_async_request(mock_async_httpx_client: Mock):
    message = ChatMessage(content="This is a test", role="user")

    mock_async_httpx_client.send.return_value = httpx.Response(
        status_code=200,
        content=json.dumps(_FAKE_RESPONSE_DICT).encode("utf-8"),
    )

    with patch.object(AWSAuthorization, AWSAuthorization.get_auth_headers.__name__, return_value=_FAKE_AUTH_HEADERS):
        client = AsyncAI21BedrockClient(http_client=mock_async_httpx_client)
        await client.chat.completions.create(model=BedrockModelID.JAMBA_INSTRUCT_V1, messages=[message])

    mock_async_httpx_client.build_request.assert_called_once_with(
        method="POST",
        url=_FULL_BEDROCK_URL,
        headers={
            "Content-Type": "application/json",
            "User-Agent": ANY,
            **_FAKE_AUTH_HEADERS,
        },
        timeout=300,
        params={},
        data=json.dumps({"messages": [message.to_dict()]}).encode("utf-8"),
        files=None,
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ids=[
        "when_sync_client__model_and_model_id__should_raise_error",
        "when_sync_client__no_model_and_no_model_id__should_raise_error",
        "when_async_client__no_model_and_no_model_id__should_raise_error",
        "when_async_client__no_model_and_no_model_id__should_raise_error",
    ],
    argvalues=[
        (BedrockModelID.JAMBA_INSTRUCT_V1, BedrockModelID.JAMBA_INSTRUCT_V1, AI21BedrockClient()),
        (None, None, AI21BedrockClient()),
        (BedrockModelID.JAMBA_INSTRUCT_V1, BedrockModelID.JAMBA_INSTRUCT_V1, AsyncAI21BedrockClient()),
        (None, None, AsyncAI21BedrockClient()),
    ],
    argnames=["model", "model_id", "client"],
)
async def test_model_id_and_model_supported_params(
    model: Optional[BedrockModelID],
    model_id: Optional[BedrockModelID],
    client: Union[AI21BedrockClient, AsyncAI21BedrockClient],
):
    with pytest.raises(ValueError):
        if isinstance(client, AsyncAI21BedrockClient):
            await client.chat.completions.create(
                model=model,
                messages=[ChatMessage(content="This is a test", role="user")],
                model_id=model_id,
            )
        else:
            client.chat.completions.create(
                model=model,
                messages=[ChatMessage(content="This is a test", role="user")],
                model_id=model_id,
            )
