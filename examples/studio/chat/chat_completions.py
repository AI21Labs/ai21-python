from ai21 import AI21Client
from ai21.models.chat.chat_message import AssistantMessage, SystemMessage, UserMessage


system = "You're a support engineer in a SaaS company"
messages = [
    SystemMessage(content=system, role="system"),
    UserMessage(content="Hello, I need help with a signup process.", role="user"),
    AssistantMessage(content="Hi Alice, I can help you with that. What seems to be the problem?", role="assistant"),
    UserMessage(content="I am having trouble signing up for your product with my Google account.", role="user"),
]

client = AI21Client()

response = client.chat.completions.create(
    messages=messages,
    model="jamba-mini",
    max_tokens=100,
    temperature=0.7,
    top_p=1.0,
    stop=["\n"],
)

print(response)
