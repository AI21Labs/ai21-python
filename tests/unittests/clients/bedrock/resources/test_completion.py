from typing import Optional

import httpx
import pytest
from unittest.mock import Mock, ANY

from ai21.clients.bedrock.resources.bedrock_completion import BedrockCompletion, AsyncBedrockCompletion

_CTOR_PROVIDED_MODEL_ID = "constructor_provided_model_id"
_INVOCATION_MODEL_ID = "invocation_model_id"
_AWS_REGION = "some-region"


@pytest.mark.parametrize(
    ids=[
        "when_model_id_not_passed_in_create__should_use_model_id_from_init",
        "when_model_id_passed_in_create__should_use_model_id_from_create",
    ],
    argnames=["invocation_model_id", "expected_model_id"],
    argvalues=[
        (None, _CTOR_PROVIDED_MODEL_ID),
        (_INVOCATION_MODEL_ID, _INVOCATION_MODEL_ID),
    ],
)
def test__when_model_id_create_and_init__should_use_one_from_create(
    invocation_model_id: Optional[str],
    expected_model_id: str,
    mock_http_client: Mock,
):
    mock_http_client.execute_http_request.return_value = httpx.Response(
        status_code=200,
        json={
            "id": expected_model_id,
            "prompt": {
                "text": "test",
                "tokens": [],
            },
            "completions": [],
        },
    )

    client = BedrockCompletion(model_id=_CTOR_PROVIDED_MODEL_ID, client=mock_http_client, region=_AWS_REGION)

    # We can not pass "None" explicitly to the create method, so we have to use the if else statement
    if invocation_model_id is None:
        client.create(prompt="test")
    else:
        client.create(model_id=invocation_model_id, prompt="test")

    mock_http_client.execute_http_request.assert_called_once_with(
        url=f"https://bedrock-runtime.some-region.amazonaws.com/model/{expected_model_id}/invoke",
        method="POST",
        body=ANY,
        extra_headers=ANY,
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ids=[
        "when_model_id_not_passed_in_create__should_use_model_id_from_init",
        "when_model_id_passed_in_create__should_use_model_id_from_create",
    ],
    argnames=["invocation_model_id", "expected_model_id"],
    argvalues=[
        (None, _CTOR_PROVIDED_MODEL_ID),
        (_INVOCATION_MODEL_ID, _INVOCATION_MODEL_ID),
    ],
)
async def test_async__when_model_id_create_and_init__should_use_one_from_create(
    invocation_model_id: Optional[str],
    expected_model_id: str,
    mock_async_http_client: Mock,
):
    mock_async_http_client.execute_http_request.return_value = httpx.Response(
        status_code=200,
        json={
            "id": expected_model_id,
            "prompt": {
                "text": "test",
                "tokens": [],
            },
            "completions": [],
        },
    )

    client = AsyncBedrockCompletion(model_id=_CTOR_PROVIDED_MODEL_ID, client=mock_async_http_client, region=_AWS_REGION)

    # We can not pass "None" explicitly to the create method, so we have to use the if else statement
    if invocation_model_id is None:
        await client.create(prompt="test")
    else:
        await client.create(model_id=invocation_model_id, prompt="test")

    mock_async_http_client.execute_http_request.assert_called_once_with(
        url=f"https://bedrock-runtime.some-region.amazonaws.com/model/{expected_model_id}/invoke",
        method="POST",
        body=ANY,
        extra_headers=ANY,
    )
