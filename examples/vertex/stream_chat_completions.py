from ai21 import AI21VertexClient

from ai21.models.chat import ChatMessage

client = AI21VertexClient()

messages = ChatMessage(content="What is the meaning of life?", role="user")

completion = client.chat.completions.create(
    model="jamba-1.5-mini",
    messages=[messages],
    stream=True,
)

for chunk in completion:
    print(chunk.choices[0].delta.content, end="")
