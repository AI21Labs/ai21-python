from ai21 import AI21AzureClient

from ai21.models.chat import ChatMessage

client = AI21AzureClient(
    base_url="<Your endpoint>",
    api_key="<your api key>",
)

messages = ChatMessage(content="What is the meaning of life?", role="user")

completion = client.chat.completions.create(
    model="jamba-instruct",
    messages=[messages],
)

print(completion.to_json())
