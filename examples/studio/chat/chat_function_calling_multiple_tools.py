import json

from ai21 import AI21Client
from ai21.models.chat import ChatMessage, ToolMessage
from ai21.models.chat.function_tool_definition import FunctionToolDefinition
from ai21.models.chat.tool_defintions import ToolDefinition
from ai21.models.chat.tool_parameters import ToolParameters

# set_verbose(True)


def get_weather(place: str, date: str) -> str:
    """
    Retrieve the expected weather for a specified location and date.
    """
    print(f"Fetching expected weather for {place} on {date}...")
    return "32 celsius"


def get_sunset_hour(place: str, date: str) -> str:
    """
    Fetch the expected sunset time for a given location and date.
    """
    print(f"Fetching expected sunset time for {place} on {date}...")
    return "7 pm"


messages = [
    ChatMessage(
        role="system",
        content="You are a helpful assistant. Use the supplied tools to assist the user.",
    ),
    ChatMessage(
        role="user", content="Hello, could you help me find out the weather forecast and sunset time for London?"
    ),
    ChatMessage(role="assistant", content="Hi there! I can help with that. On which date?"),
    ChatMessage(role="user", content="At 2024-08-27"),
]

get_sunset_tool = ToolDefinition(
    type="function",
    function=FunctionToolDefinition(
        name="get_sunset_hour",
        description="Fetch the expected sunset time for a given location and date.",
        parameters=ToolParameters(
            type="object",
            properties={
                "place": {"type": "string", "description": "The location for which the weather is being queried."},
                "date": {"type": "string", "description": "The date for which the weather is being queried."},
            },
            required=["place", "date"],
        ),
    ),
)

get_weather_tool = ToolDefinition(
    type="function",
    function=FunctionToolDefinition(
        name="get_weather",
        description="Retrieve the expected weather for a specified location and date.",
        parameters=ToolParameters(
            type="object",
            properties={
                "place": {"type": "string", "description": "The location for which the weather is being queried."},
                "date": {"type": "string", "description": "The date for which the weather is being queried."},
            },
            required=["place", "date"],
        ),
    ),
)

tools = [get_sunset_tool, get_weather_tool]

client = AI21Client(api_host="https://api-stage.ai21.com", api_key="F6iFeKlMsisusyhtoy1ZUj4bRPhEd6sf")

response = client.chat.completions.create(messages=messages, model="jamba-1.5-large", tools=tools)

""" AI models can be error-prone, it's crucial to ensure that the tool calls align with the expectations.
The below code snippet demonstrates how to handle tool calls in the response and invoke the tool function
to get the delivery date for the user's order. After retrieving the delivery date, we pass the response back
to the AI model to continue the conversation, using the ToolMessage object. """

assistant_message = response.choices[0].message
messages.append(assistant_message)  # Adding the assistant message to the chat history


too_call_id_to_result = {}
tool_calls = assistant_message.tool_calls
if tool_calls:
    for tool_call in tool_calls:
        if tool_call.function.name == "get_weather":
            """Verify get_weather tool call arguments and invoke the function to get the weather forecast:"""
            func_arguments = tool_call.function.arguments
            args = json.loads(func_arguments)

            if "place" in args and "date" in args:
                result = get_weather(args["place"], args["date"])
                too_call_id_to_result[tool_call.id] = result
            else:
                print(f"Got unexpected arguments in function call - {args}")

        elif tool_call.function.name == "get_sunset_hour":
            """Verify get_sunset_hour tool call arguments and invoke the function to get the weather forecast:"""
            func_arguments = tool_call.function.arguments
            args = json.loads(func_arguments)

            if "place" in args and "date" in args:
                result = get_sunset_hour(args["place"], args["date"])
                too_call_id_to_result[tool_call.id] = result
            else:
                print(f"Got unexpected arguments in function call - {args}")

        else:
            print(f"Unexpected tool call found - {tool_call.function.name}")
else:
    print("No tool calls found")


if too_call_id_to_result:
    """Continue the conversation by passing the sunset and weather back to the AI model:"""

    for tool_id_called, result in too_call_id_to_result.items():
        tool_message = ToolMessage(role="tool", tool_call_id=tool_id_called, content=str(result))
        messages.append(tool_message)

    response = client.chat.completions.create(messages=messages, model="jamba-1.5-large", tools=tools)
    print(response.choices[0].message.content)
