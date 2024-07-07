import pytest
from ai21 import AI21Client, AsyncAI21Client
from ai21.models import ChatMessage, RoleType

_DUMMY_API_KEY = "dummy_api_key"


def test_chat_create__when_bad_import_to_chat_message__raise_error():
    with pytest.raises(ValueError) as e:
        AI21Client(api_key=_DUMMY_API_KEY).chat.completions.create(
            model="jamba-instruct-preview",
            messages=[ChatMessage(role=RoleType.USER, text="Hello")],
            system="System Test",
        )

    assert (
        e.value.args[0] == "Please use the ChatMessage class from ai21.models.chat instead"
        " of ai21.models when working with chat completions."
    )


@pytest.mark.asyncio
async def test_async_chat_create__when_bad_import_to_chat_message__raise_error():
    with pytest.raises(ValueError) as e:
        await AsyncAI21Client(api_key=_DUMMY_API_KEY).chat.completions.create(
            model="jamba-instruct-preview",
            messages=[ChatMessage(role=RoleType.USER, text="Hello")],
            system="System Test",
        )

    assert (
        e.value.args[0] == "Please use the ChatMessage class from ai21.models.chat instead"
        " of ai21.models when working with chat completions."
    )


def test__when_model_and_model_id__raise_error():
    client = AI21Client()
    with pytest.raises(ValueError):
        client.chat.completions.create(
            model="jamba-instruct",
            model_id="jamba-instruct",
            messages=[ChatMessage(role=RoleType.USER, text="Hello")],
        )
