import uuid

from unittest.mock import AsyncMock

import httpx
import pytest

from pytest_mock import MockerFixture

from ai21 import AI21Client, AsyncAI21Client
from ai21.models import ChatMessage, RoleType
from ai21.models.chat import ChatCompletionResponse, ResponseFormat
from ai21.models.chat.chat_message import AssistantMessage, SystemMessage, UserMessage
from ai21.models.chat.document_schema import DocumentSchema
from ai21.models.chat.function_tool_definition import FunctionToolDefinition
from ai21.models.chat.tool_defintions import ToolDefinition
from ai21.models.chat.tool_parameters import ToolParameters


_FAKE_API_KEY = "dummy_api_key"


def test_chat_create__when_bad_import_to_chat_message__raise_error():
    with pytest.raises(ValueError) as e:
        AI21Client(api_key=_FAKE_API_KEY).chat.completions.create(
            model="jamba-1.5",
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
        await AsyncAI21Client(api_key=_FAKE_API_KEY).chat.completions.create(
            model="jamba-1.5",
            messages=[ChatMessage(role=RoleType.USER, text="Hello")],
            system="System Test",
        )

    assert (
        e.value.args[0] == "Please use the ChatMessage class from ai21.models.chat instead"
        " of ai21.models when working with chat completions."
    )


# ----------------------------------- Basic Happy Flow: ----------------------------------- #

_FAKE_BASIC_HAPPY_FLOW_RESPONSE_JSON = {
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

_FAKE_BASIC_HAPPY_FLOW_EXPECTED_CONTENT = " Hello! How can I assist you today?"


def test_chat_completion_basic_happy_flow(mocker: MockerFixture) -> None:
    mocked_client = mocker.Mock(spec=httpx.Client)
    mocked_client.send.return_value = httpx.Response(status_code=200, json=_FAKE_BASIC_HAPPY_FLOW_RESPONSE_JSON)
    client = AI21Client(api_key=_FAKE_API_KEY, http_client=mocked_client)
    response: ChatCompletionResponse = client.chat.completions.create(
        model="jamba-1.6-mini-2025-03", messages=[UserMessage(role="user", content="Hello")]
    )
    assert response.choices[0].message.content == _FAKE_BASIC_HAPPY_FLOW_EXPECTED_CONTENT


@pytest.mark.asyncio
async def test_async_chat_completion_basic_happy_flow(mocker: MockerFixture) -> None:
    mocked_client = mocker.Mock(spec=httpx.Client)
    mocked_client.send = AsyncMock(
        return_value=httpx.Response(status_code=200, json=_FAKE_BASIC_HAPPY_FLOW_RESPONSE_JSON)
    )
    async_client = AsyncAI21Client(api_key=_FAKE_API_KEY, http_client=mocked_client)
    response: ChatCompletionResponse = await async_client.chat.completions.create(
        model="jamba-1.6-mini-2025-03", messages=[UserMessage(role="user", content="Hello")]
    )
    assert response.choices[0].message.content == _FAKE_BASIC_HAPPY_FLOW_EXPECTED_CONTENT


# ----------------------------------- Tool Calls Happy Flow: ----------------------------------- #

_FAKE_TOOL_CALLS_HAPPY_FLOW_RESPONSE_JSON = {
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

_FAKE_TOOL_CALL_TEST_MESSAGES = [
    SystemMessage(
        role="system",
        content="You are a helpful customer support assistant. Use the supplied tools to assist the user.",
    ),
    UserMessage(role="user", content="Hi, can you tell me the delivery date for my order?"),
    AssistantMessage(role="assistant", content="Hi there! I can help with that. Can you please provide your order ID?"),
    UserMessage(role="user", content="i think it is order_12345"),
]

_FAKE_TOOL_CALL_TEST_TOOLS = [
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

_FAKE_TOOL_CALL_TEST_EXPECTED_FUNCTION_NAME = "get_delivery_date"
_FAKE_TOOL_CALL_TEST_EXPECTED_FUNCTION_ARGUMENTS = '{"order_id":"order_12345"}'


def test_chat_completion_with_tool_calls_happy_flow(mocker: MockerFixture) -> None:
    mocked_client = mocker.Mock(spec=httpx.Client)
    mocked_client.send.return_value = httpx.Response(status_code=200, json=_FAKE_TOOL_CALLS_HAPPY_FLOW_RESPONSE_JSON)
    client = AI21Client(api_key=_FAKE_API_KEY, http_client=mocked_client)
    response = client.chat.completions.create(
        model="jamba-1.6-mini-2025-03", messages=_FAKE_TOOL_CALL_TEST_MESSAGES, tools=_FAKE_TOOL_CALL_TEST_TOOLS
    )
    assert response.choices[0].message.tool_calls[0].function.name == _FAKE_TOOL_CALL_TEST_EXPECTED_FUNCTION_NAME
    assert (
        response.choices[0].message.tool_calls[0].function.arguments == _FAKE_TOOL_CALL_TEST_EXPECTED_FUNCTION_ARGUMENTS
    )


@pytest.mark.asyncio
async def test_async_chat_completion_with_tool_calls_happy_flow(mocker: MockerFixture) -> None:
    mocked_client = mocker.Mock(spec=httpx.Client)
    mocked_client.send = AsyncMock(
        return_value=httpx.Response(status_code=200, json=_FAKE_TOOL_CALLS_HAPPY_FLOW_RESPONSE_JSON)
    )
    async_client = AsyncAI21Client(api_key=_FAKE_API_KEY, http_client=mocked_client)
    response = await async_client.chat.completions.create(
        model="jamba-1.6-mini-2025-03", messages=_FAKE_TOOL_CALL_TEST_MESSAGES, tools=_FAKE_TOOL_CALL_TEST_TOOLS
    )
    assert response.choices[0].message.tool_calls[0].function.name == _FAKE_TOOL_CALL_TEST_EXPECTED_FUNCTION_NAME
    assert (
        response.choices[0].message.tool_calls[0].function.arguments == _FAKE_TOOL_CALL_TEST_EXPECTED_FUNCTION_ARGUMENTS
    )


# ----------------------------------- Documents Happy Flow: ----------------------------------- #

_FAKE_DOCUMENTS_TEST_RESPONSE_JSON = {
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

_FAKE_DOCUMENTS_TEST_DOCUMENTS = [schnoodel, shnokel]

_FAKE_DOCUMENTS_TEST_MESSAGES = [
    SystemMessage(
        role="system",
        content="You are a helpful assistant that receives revenue documents and answers related questions",
    ),
    UserMessage(role="user", content="Hi, which company earned more during 2024 - Schnoodel or Shnokel?"),
]

_FAKE_DOCUMENTS_TEST_EXPECTED_CONTENT = "Shnokel."


def test_chat_completion_with_documents_happy_flow(mocker: MockerFixture) -> None:
    mocked_client = mocker.Mock(spec=httpx.Client)
    mocked_client.send.return_value = httpx.Response(status_code=200, json=_FAKE_DOCUMENTS_TEST_RESPONSE_JSON)
    client = AI21Client(api_key=_FAKE_API_KEY, http_client=mocked_client)
    response = client.chat.completions.create(
        model="jamba-1.6-mini-2025-03", messages=_FAKE_DOCUMENTS_TEST_MESSAGES, documents=_FAKE_DOCUMENTS_TEST_DOCUMENTS
    )
    assert response.choices[0].message.content == _FAKE_DOCUMENTS_TEST_EXPECTED_CONTENT


@pytest.mark.asyncio
async def test_async_chat_completion_with_documents_happy_flow(mocker: MockerFixture) -> None:
    mocked_client = mocker.Mock(spec=httpx.Client)
    mocked_client.send = AsyncMock(
        return_value=httpx.Response(status_code=200, json=_FAKE_DOCUMENTS_TEST_RESPONSE_JSON)
    )
    async_client = AsyncAI21Client(api_key=_FAKE_API_KEY, http_client=mocked_client)
    response = await async_client.chat.completions.create(
        model="jamba-1.6-mini-2025-03", messages=_FAKE_DOCUMENTS_TEST_MESSAGES, documents=_FAKE_DOCUMENTS_TEST_DOCUMENTS
    )
    assert response.choices[0].message.content == _FAKE_DOCUMENTS_TEST_EXPECTED_CONTENT


# ----------------------------------- Response Format JSON Happy Flow: ----------------------------------- #

_FAKE_RESPONSE_FORMAT_JSON_TEST_MESSAGES = [
    UserMessage(
        role="user",
        content="Please create a JSON object for ordering zoo tickets for September 22, 2024, "
        "for myself and two kids, based on the following JSON schema: "
        "{'$defs': {'TicketType': {'enum': ['adult', 'child'], "
        "'title': 'TicketType', 'type': 'string'}, 'ZooTicket': "
        "{'properties': {'ticket_type': {'$ref': '#/$defs/TicketType'}, "
        "'quantity': {'title': 'Quantity', 'type': 'integer'}}, "
        "'required': ['ticket_type', 'quantity'], 'title': 'ZooTicket', "
        "'type': 'object'}}, 'properties': {'date': {'title': 'Date', 'type': 'string'}, "
        "'tickets': {'items': {'$ref': '#/$defs/ZooTicket'}, 'title': 'Tickets', "
        "'type': 'array'}}, 'required': ['date', 'tickets'], 'title': "
        "'ZooTicketsOrder', 'type': 'object'}.",
    )
]


_FAKE_RESPONSE_FORMAT_JSON_TEST_RESPONSE_JSON = {
    "id": "chat-6e39bb45b50e453b9825ee984c554821",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": '{"date": "2024-09-22","tickets":'
                '[{"ticket_type": "adult","quantity": 1},{"ticket_type": "child","quantity": 2}]}',
                "tool_calls": None,
                "logprobs": None,
                "finish_reason": "stop",
            },
        }
    ],
    "usage": {"prompt_tokens": 311, "completion_tokens": 81, "total_tokens": 392},
}

_FAKE_RESPONSE_FORMAT_JSON_TEST_EXPECTED_CONTENT = (
    '{"date": "2024-09-22","tickets":'
    '[{"ticket_type": "adult","quantity": 1},'
    '{"ticket_type": "child","quantity": 2}]}'
)


def test_chat_completion_response_format_json_happy_flow(mocker: MockerFixture) -> None:
    mocked_client = mocker.Mock(spec=httpx.Client)
    mocked_client.send.return_value = httpx.Response(
        status_code=200, json=_FAKE_RESPONSE_FORMAT_JSON_TEST_RESPONSE_JSON
    )
    client = AI21Client(api_key=_FAKE_API_KEY, http_client=mocked_client)
    response = client.chat.completions.create(
        model="jamba-1.6-mini-2025-03",
        messages=_FAKE_RESPONSE_FORMAT_JSON_TEST_MESSAGES,
        response_format=ResponseFormat(type="json_object"),
    )
    assert response.choices[0].message.content == _FAKE_RESPONSE_FORMAT_JSON_TEST_EXPECTED_CONTENT


@pytest.mark.asyncio
async def test_async_chat_completion_response_format_json_happy_flow(mocker: MockerFixture) -> None:
    mocked_client = mocker.Mock(spec=httpx.Client)
    mocked_client.send = AsyncMock(
        return_value=httpx.Response(status_code=200, json=_FAKE_RESPONSE_FORMAT_JSON_TEST_RESPONSE_JSON)
    )
    async_client = AsyncAI21Client(api_key=_FAKE_API_KEY, http_client=mocked_client)
    response = await async_client.chat.completions.create(
        model="jamba-1.6-mini-2025-03",
        messages=_FAKE_RESPONSE_FORMAT_JSON_TEST_MESSAGES,
        response_format=ResponseFormat(type="json_object"),
    )
    assert response.choices[0].message.content == _FAKE_RESPONSE_FORMAT_JSON_TEST_EXPECTED_CONTENT
