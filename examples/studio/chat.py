from ai21 import AI21Client

system = "You're a support engineer in a SaaS company"
messages = [
    {
        "text": "Hello, I need help with a signup process.",
        "role": "user",
        "name": "Alice",
    },
    {
        "text": "Hi Alice, I can help you with that. What seems to be the problem?",
        "role": "assistant",
        "name": "Bob",
    },
    {
        "text": "I am having trouble signing up for your product with my Google account.",
        "role": "user",
        "name": "Alice",
    },
]

client = AI21Client()
response = client.chat.create(system=system, messages=messages, model="j2-ultra")

print(response)
