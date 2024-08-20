from ai21 import AI21Client
from ai21.logger import set_verbose
from ai21.models.chat import ChatMessage, ToolMessage
from ai21.models.chat.function_tool_definition import FunctionToolDefinition
from ai21.models.chat.tool_defintions import ToolDefinition
from ai21.models.chat.tool_parameters import ToolParameters

set_verbose(True)


def get_order_delivery_date(order_id: str) -> str:
    print(f"Getting delivery date from database for order ID: {order_id}...")
    return "2025-05-04"


messages = [
    ChatMessage(
        role="system",
        content="You are a helpful customer support assistant. Use the supplied tools to assist the user.",
    ),
    ChatMessage(role="user", content="Hi, can you tell me the delivery date for my order?"),
    ChatMessage(role="assistant", content="Hi there! I can help with that. Can you please provide your order ID?"),
    ChatMessage(role="user", content="i think it is order_12345"),
]

tool_definition = ToolDefinition(
    type="function",
    function=FunctionToolDefinition(
        name="get_order_delivery_date",
        description="Get the delivery date for a given order ID",
        parameters=ToolParameters(
            type="object",
            properties={"order_id": {"type": "string", "description": "The customer's order ID."}},
            required=["order_id"],
        ),
    ),
)

tools = [tool_definition]

client = AI21Client(api_host="https://api-stage.ai21.com", api_key="F6iFeKlMsisusyhtoy1ZUj4bRPhEd6sf")

response = client.chat.completions.create(messages=messages, model="jamba-1.5-large", tools=tools)

print(response)

assistant_message = response.choices[0].message
tool_calls = assistant_message.tool_calls

delivery_date = None
if tool_calls:
    tool_call = tool_calls[0]
    if tool_call.function.name == "get_order_delivery_date":
        func_arguments = tool_call.function.arguments
        if "order_id" in func_arguments:
            # extract the order ID from the function arguments logic... (in this case it's just 1 argument)
            order_id = func_arguments
            delivery_date = get_order_delivery_date(order_id)
            print(f"Delivery date for order ID {order_id}: {delivery_date}")
        else:
            print("order_id not found in function arguments")
    else:
        print(f"Unexpected tool call found - {tool_call.function.name}")
else:
    print("No tool calls found.")

if delivery_date is not None:
    tool_message = ToolMessage(role="tool", tool_call_id=tool_calls[0].id, content=delivery_date)
    messages.append(assistant_message)
    messages.append(tool_message)
    response = client.chat.completions.create(messages=messages, model="jamba-1.5-large", tools=tools)
    print(response)
