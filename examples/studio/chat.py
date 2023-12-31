from ai21 import AI21Client
from ai21.resources import Message, RoleType, Penalty

system = "You're a support engineer in a SaaS company"
messages = [
    Message(text="Hello, I need help with a signup process.", role=RoleType.USER, name="Alice"),
    Message(
        text="Hi Alice, I can help you with that. What seems to be the problem?", role=RoleType.ASSISTANT, name="Bob"
    ),
    Message(
        text="I am having trouble signing up for your product with my Google account.", role=RoleType.USER, name="Alice"
    ),
]

client = AI21Client()
response = client.chat.create(
    system=system,
    messages=messages,
    model="j2-ultra",
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
