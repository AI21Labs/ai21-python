import uuid

import httpx
import pytest
from pytest_mock import MockerFixture

from ai21 import AI21Client, AsyncAI21Client
from ai21.models import ChatMessage, RoleType
from ai21.models.chat import ChatCompletionResponse
from ai21.models.chat.chat_message import UserMessage, SystemMessage, AssistantMessage
from ai21.models.chat.document_schema import DocumentSchema
from ai21.models.chat.function_tool_definition import FunctionToolDefinition
from ai21.models.chat.tool_defintions import ToolDefinition
from ai21.models.chat.tool_parameters import ToolParameters

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


def test_chat_completion_tools_call_happy_flow():
    client = AI21Client()
    with pytest.raises(ValueError):
        client.chat.completions.create(
            model="jamba-instruct", model_id="jamba-instruct", messages=[ChatMessage(role=RoleType.USER, text="Hello")]
        )


def test_chat_completion_basic_happy_flow(mocker: MockerFixture) -> None:
    response_json = {
        "id": "chat-cc8ce5c05f1d4ed9b722123ac4a0f267",
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": " Hello! How can I assist you today?"},
                "finish_reason": "stop",
            }
        ],
        "usage": {"prompt_tokens": 144, "completion_tokens": 14, "total_tokens": 158},
        "meta": {"requestDurationMillis": 236},
    }
    mocked_client = mocker.Mock(spec=httpx.Client)
    mocked_client.send.return_value = httpx.Response(status_code=200, json=response_json)
    client = AI21Client(api_key=_DUMMY_API_KEY, http_client=mocked_client)
    response: ChatCompletionResponse = client.chat.completions.create(
        model="jamba-1.5", messages=[UserMessage(role="user", content="Hello")]
    )
    assert response.choices[0].message.content == " Hello! How can I assist you today?"


def test_chat_completion_with_tool_calls_happy_flow(mocker: MockerFixture) -> None:
    response_json = {
        "id": "chat-cc8ce5c05f1d4ed9b722123ac4a0f267",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": None,
                    "tool_calls": [
                        {
                            "id": "call_62136354",
                            "type": "function",
                            "function": {"name": "get_delivery_date", "arguments": '{"order_id":"order_12345"}'},
                        }
                    ],
                },
                "finish_reason": "tool_calls",
            }
        ],
        "usage": {"prompt_tokens": 144, "completion_tokens": 14, "total_tokens": 158},
        "meta": {"requestDurationMillis": 236},
    }
    mocked_client = mocker.Mock(spec=httpx.Client)
    mocked_client.send.return_value = httpx.Response(status_code=200, json=response_json)
    client = AI21Client(api_key=_DUMMY_API_KEY, http_client=mocked_client)

    messages = [
        SystemMessage(
            role="system",
            content="You are a helpful customer support assistant. Use the supplied tools to assist the user.",
        ),
        UserMessage(role="user", content="Hi, can you tell me the delivery date for my order?"),
        AssistantMessage(
            role="assistant", content="Hi there! I can help with that. Can you please provide your order ID?"
        ),
        UserMessage(role="user", content="i think it is order_12345"),
    ]

    tools = [
        ToolDefinition(
            type="function",
            function=FunctionToolDefinition(
                name="get_delivery_date",
                description="Get the delivery date for a given order ID",
                parameters=ToolParameters(
                    type="object",
                    properties={"order_id": {"type": "string", "description": "The customer's order ID."}},
                    required=["order_id"],
                ),
            ),
        )
    ]

    response = client.chat.completions.create(model="jamba-1.5", messages=messages, tools=tools)
    assert response.choices[0].message.tool_calls[0].function.name == "get_delivery_date"
    assert response.choices[0].message.tool_calls[0].function.arguments == '{"order_id":"order_12345"}'


def test_chat_completion_with_documents_happy_flow(mocker: MockerFixture) -> None:
    response_json = {
        "id": "chat-cc8ce5c05f1d4ed9b722123ac4a0f267",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "Shnokel.",
                },
                "finish_reason": "stop",
            }
        ],
        "usage": {"prompt_tokens": 144, "completion_tokens": 14, "total_tokens": 158},
        "meta": {"requestDurationMillis": 236},
    }
    mocked_client = mocker.Mock(spec=httpx.Client)
    mocked_client.send.return_value = httpx.Response(status_code=200, json=response_json)
    client = AI21Client(api_key=_DUMMY_API_KEY, http_client=mocked_client)

    schnoodel = DocumentSchema(
        id=str(uuid.uuid4()),
        content="Schnoodel Inc. Annual Report - 2024. Schnoodel Inc., a leader in innovative culinary technology, "
        "saw a 15% revenue growth this year, reaching $120 million. The launch of SchnoodelChef Pro has significantly "
        "contributed, making up 35% of total sales. We've expanded into the Asian market, notably Japan, "
        "and increased our global presence. Committed to sustainability, we reduced our carbon footprint "
        "by 20%. Looking ahead, we plan to integrate more advanced machine learning features and expand "
        "into South America.",
        metadata={"topic": "revenue"},
    )
    shnokel = DocumentSchema(
        id=str(uuid.uuid4()),
        content="Shnokel Corp. TL;DR Annual Report - 2024. Shnokel Corp., a pioneer in renewable energy solutions, "
        "reported a 20% increase in revenue this year, reaching $200 million. The successful deployment of "
        "our advanced solar panels, SolarFlex, accounted for 40% of our sales. We entered new markets in Europe "
        "and have plans to develop wind energy projects next year. Our commitment to reducing environmental "
        "impact saw a 25% decrease in operational emissions. Upcoming initiatives include a significant "
        "investment in R&D for sustainable technologies.",
        metadata={"topic": "revenue"},
    )

    documents = [schnoodel, shnokel]

    messages = [
        SystemMessage(
            role="system",
            content="You are a helpful assistant that receives revenue documents and answers related questions",
        ),
        UserMessage(role="user", content="Hi, which company earned more during 2024 - Schnoodel or Shnokel?"),
    ]

    response = client.chat.completions.create(model="jamba-1.5", messages=messages, documents=documents)
    assert response.choices[0].message.content == "Shnokel."
