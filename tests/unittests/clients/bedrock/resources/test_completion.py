from typing import Optional

import pytest
from pytest_mock import MockerFixture
from unittest.mock import Mock, ANY

from ai21.clients.bedrock.resources.bedrock_completion import BedrockCompletion
from ai21.models import Prompt

_TEST_MODEL_ID = "test_model_id"
_TEST_NEW_MODEL_ID = "new_model_id"


@pytest.mark.parametrize(
    ids=[
        "when_model_id_not_passed_in_create__should_use_model_id_from_init",
        "when_model_id_passed_in_create__should_use_model_id_from_create",
    ],
    argnames=["new_model_id", "expected_model_id"],
    argvalues=[
        (None, _TEST_MODEL_ID),
        (_TEST_NEW_MODEL_ID, _TEST_NEW_MODEL_ID),
    ],
)
def test__when_model_id_create_and_init__should_use_one_from_create(
    new_model_id: Optional[str],
    expected_model_id: str,
    mock_bedrock_session: Mock,
    mocker: MockerFixture,
):
    mock_bedrock_session.invoke_model.return_value = {
        "id": expected_model_id,
        "prompt": mocker.MagicMock(spec=Prompt),
        "completions": [],
    }

    client = BedrockCompletion(model_id=_TEST_MODEL_ID, bedrock_session=mock_bedrock_session)

    # We can not pass "None" explicitly to the create method, so we have to use the if else statement
    if new_model_id is None:
        client.create(prompt="test")
    else:
        client.create(model_id=new_model_id, prompt="test")

    mock_bedrock_session.invoke_model.assert_called_once_with(model_id=expected_model_id, input_json=ANY)
