from ai21 import AI21LaunchpadClient
from ai21.models.chat import ChatMessage


client = AI21LaunchpadClient(endpoint_id="<your_endpoint_id>")

messages = ChatMessage(content="What is the meaning of life?", role="user")

completion = client.chat.completions.create(
    model="jamba-1.6-large",
    messages=[messages],
    stream=True,
)


print(completion)
