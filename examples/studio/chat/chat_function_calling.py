import json

from ai21 import AI21Client
from ai21.logger import set_verbose
from ai21.models.chat import (
    ChatMessage,
    FunctionToolDefinition,
    ToolDefinition,
    ToolMessage,
    ToolParameters,
)


set_verbose(True)


def get_order_delivery_date(order_id: str) -> str:
    print(f"Retrieving the delivery date for order ID: {order_id} from the database...")
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
        description="Retrieve the delivery date associated with the specified order ID",
        parameters=ToolParameters(
            type="object",
            properties={"order_id": {"type": "string", "description": "The customer's order ID."}},
            required=["order_id"],
        ),
    ),
)

tools = [tool_definition]

client = AI21Client()

response = client.chat.completions.create(messages=messages, model="jamba-large", tools=tools)

""" AI models can be error-prone, it's crucial to ensure that the tool calls align with the expectations.
The below code snippet demonstrates how to handle tool calls in the response and invoke the tool function
to get the delivery date for the user's order. After retrieving the delivery date, we pass the response back
to the AI model to continue the conversation, using the ToolMessage object. """

assistant_message = response.choices[0].message
messages.append(assistant_message)  # Adding the assistant message to the chat history

delivery_date = None
tool_calls = assistant_message.tool_calls
if tool_calls:
    tool_call = tool_calls[0]
    if tool_call.function.name == "get_order_delivery_date":
        func_arguments = tool_call.function.arguments
        func_args_dict = json.loads(func_arguments)

        if "order_id" in func_args_dict:
            delivery_date = get_order_delivery_date(func_args_dict["order_id"])
        else:
            print("order_id not found in function arguments")
    else:
        print(f"Unexpected tool call found - {tool_call.function.name}")
else:
    print("No tool calls found")

if delivery_date is not None:
    """Continue the conversation by passing the delivery date back to the model"""

    tool_message = ToolMessage(role="tool", tool_call_id=tool_calls[0].id, content=delivery_date)
    messages.append(tool_message)

    response = client.chat.completions.create(messages=messages, model="jamba-large", tools=tools)
    print(response.choices[0].message.content)
