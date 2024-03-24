from ai21 import AI21Client
from ai21.models import ChatMessage, RoleType, Penalty

system = "You're a support engineer in a SaaS company"
messages = [
    ChatMessage(content="Hello, I need help with a signup process.", role=RoleType.USER),
    ChatMessage(content="Hi Alice, I can help you with that. What seems to be the problem?", role=RoleType.ASSISTANT),
    ChatMessage(content="I am having trouble signing up for your product with my Google account.", role=RoleType.USER),
]

client = AI21Client()
response = client.chat.create(
    system=system,
    messages=messages,
    model="j2-mid",
    count_penalty=Penalty(
        scale=0,
        apply_to_emojis=False,
        apply_to_numbers=False,
        apply_to_stopwords=False,
        apply_to_punctuation=False,
        apply_to_whitespaces=False,
    ),
)

print(response)
