from ai21 import AI21Client
from ai21.models.chat import ChatMessage
from ai21.models.chat.function_tool_definition import FunctionToolDefinition
from ai21.models.chat.tool_defintions import ToolDefinition
from ai21.models.chat.tool_parameters import ToolParameters

messages = [
    ChatMessage(
        role="system",
        content="You are a helpful customer support assistant. Use the supplied tools to assist the user.",
    ),
    ChatMessage(role="user", content="Hi, can you tell me the delivery date for my order?"),
    ChatMessage(role="assistant", content="Hi there! I can help with that. Can you please provide your order ID?"),
    ChatMessage(role="user", content="i think it is order_12345"),
]

tools = [
    ToolDefinition(
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
]

client = AI21Client()

response = client.chat.completions.create(messages=messages, model="jamba-instruct", tools=tools)

print(response)
