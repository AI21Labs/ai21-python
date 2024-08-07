from ai21 import AI21VertexClient

from ai21.models.chat import ChatMessage

client = AI21VertexClient()

messages = ChatMessage(content="What is the meaning of life?", role="user")

completion = client.chat.completions.create(
    model="jamba-instruct",
    messages=[messages],
)

print(completion.to_json())
