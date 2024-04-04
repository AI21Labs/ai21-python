from ai21 import AI21Client
from ai21.models.chat import ChatMessage

system = "You're a support engineer in a SaaS company"
messages = [
    ChatMessage(content="Hello, I need help with a signup process.", role="user"),
    ChatMessage(content="Hi Alice, I can help you with that. What seems to be the problem?", role="assistant"),
    ChatMessage(content="I am having trouble signing up for your product with my Google account.", role="user"),
]

client = AI21Client()

response = client.chat.completions.create(
    messages=messages,
    model="new-model-name",
    n=2,
    logprobs=True,
    top_logprobs=2,
    max_tokens=100,
    temperature=0.7,
    top_p=1.0,
    stop=["\n"],
    frequency_penalty=0.1,
    presence_penalty=0.1,
)

print(response)
