from ai21 import AI21BedrockClient, BedrockModelID
from ai21.models.chat import ChatMessage

# Bedrock is currently supported only in us-east-1 region.
# Either set your profile's region to us-east-1 or uncomment next line
# ai21.aws_region = 'us-east-1'
# Or create a boto session and pass it:
# import boto3
# session = boto3.Session(region_name="us-east-1")

system = "You're a support engineer in a SaaS company"
messages = [
    ChatMessage(content=system, role="system"),
    ChatMessage(content="Hello, I need help with a signup process.", role="user"),
    ChatMessage(content="Hi Alice, I can help you with that. What seems to be the problem?", role="assistant"),
    ChatMessage(content="I am having trouble signing up for your product with my Google account.", role="user"),
]

client = AI21BedrockClient()

response = client.chat.completions.create(
    messages=messages,
    max_tokens=1000,
    temperature=0,
    model=BedrockModelID.JAMBA_INSTRUCT_V1,
)

print(f"response: {response}")
