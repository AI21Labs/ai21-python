import json

from ai21 import AI21Client
from ai21.logger import set_verbose
from ai21.models.chat import ChatMessage, ToolMessage
from ai21.models.chat.function_tool_definition import FunctionToolDefinition
from ai21.models.chat.tool_defintions import ToolDefinition
from ai21.models.chat.tool_parameters import ToolParameters

set_verbose(True)


def get_weather(place: str, date: str) -> str:
    print(f"Getting the expected weather at {place} during {date} from the internet...")
    return "32 celsius"


def get_sunset_hour(place: str, date: str):
    print(f"Getting the expected sunset hour at {place} during {date} from the internet...")
    return "7 pm"


messages = [
    ChatMessage(
        role="system",
        content="You are a helpful assistant. Use the supplied tools to assist the user.",
    ),
    ChatMessage(
        role="user", content="Hi, can you assist me to get info about the weather and expected sunset in Tel Aviv?"
    ),
    ChatMessage(role="assistant", content="Hi there! I can help with that. On which date?"),
    ChatMessage(role="user", content="At 2024-08-27"),
]

get_sunset_tool = ToolDefinition(
    type="function",
    function=FunctionToolDefinition(
        name="get_sunset_hour",
        description="Search the internet for the sunset hour at a given place on a given date",
        parameters=ToolParameters(
            type="object",
            properties={
                "place": {"type": "string", "description": "The place to look for the weather at"},
                "date": {"type": "string", "description": "The date to look for the weather at"},
            },
            required=["place", "date"],
        ),
    ),
)

get_weather_tool = ToolDefinition(
    type="function",
    function=FunctionToolDefinition(
        name="get_weather",
        description="Search the internet for the weather at a given place on a given date",
        parameters=ToolParameters(
            type="object",
            properties={
                "place": {"type": "string", "description": "The place to look for the weather at"},
                "date": {"type": "string", "description": "The date to look for the weather at"},
            },
            required=["place", "date"],
        ),
    ),
)

tools = [get_sunset_tool, get_weather_tool]

client = AI21Client()

response = client.chat.completions.create(messages=messages, model="jamba-1.5-large", tools=tools)

print(response.choices[0].message)

assistant_message = response.choices[0].message
messages.append(assistant_message)

tool_calls = assistant_message.tool_calls

too_call_id_to_result = {}
if tool_calls:
    for tool_call in tool_calls:
        if tool_call.function.name == "get_weather":
            func_arguments = tool_call.function.arguments
            args = json.loads(func_arguments)
            if "place" in args and "date" in args:
                result = get_weather(args["place"], args["date"])
                too_call_id_to_result[tool_call.id] = result
            else:
                print(f"Got unexpected arguments in function call - {args}")
        elif tool_call.function.name == "get_sunset_hour":
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
    print("No tool calls found.")


if too_call_id_to_result:
    for tool_id_called, result in too_call_id_to_result.items():
        tool_message = ToolMessage(role="tool", tool_call_id=tool_id_called, content=str(result))
        messages.append(tool_message)

    for message in messages:
        print(message)

    response = client.chat.completions.create(messages=messages, model="jamba-1.5-large", tools=tools)
    print(response.choices[0].message)
