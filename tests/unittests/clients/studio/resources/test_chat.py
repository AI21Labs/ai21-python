import pytest
from ai21 import AI21Client
from ai21.models.chat import ChatMessage

_DUMMY_API_KEY = "dummy_api_key"


def test_chat_create__when_bad_import_to_chat_message__raise_error():
    with pytest.raises(ValueError) as e:
        AI21Client(api_key=_DUMMY_API_KEY).chat.create(
            model="j2-ultra", messages=[ChatMessage(role="user", content="Hello")], system="System Test"
        )

    assert (
        e.value.args[0]
        == "Please use the ChatMessage class from ai21.models instead of ai21.models.chat when working with chat"
    )
