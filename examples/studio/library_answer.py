from ai21 import AI21Client


client = AI21Client()
response = client.library.answer.create(question="Tell me something about Holland")
print(response)
